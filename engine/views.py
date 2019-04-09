from django.shortcuts import render, redirectfrom django.http import JsonResponsefrom django.shortcuts import get_object_or_404, render_to_responsefrom django.core.exceptions import ObjectDoesNotExistfrom django.core.serializers import serializefrom datetime import datetimefrom .cart import Cartfrom .forms import contactForm, ProductFormfrom django.db.models import Qfrom .config import paginationfrom .models import Product, StoreDatabase, MtgDatabasefrom functools import reducefrom operator import or_from .tcgplayer import card_price, search_inventory, price_for_rarity, card_price_single, TcgPlayerApifrom customer.models import ItemizedPreorderimport refrom decimal import Decimalfrom customer.tasks import send_orderfrom ppal.paypal_api import PaypalApifrom ppal.models import PaypalOrderimport astfrom django.urls import reversefrom customer.models import Customer, PreordersReady, Preorderfrom .tasks import complete_ordertcg = TcgPlayerApi()paypal = PaypalApi()def home_base(request):    cart = Cart(request)    cart_length = cart.cart_length    response = render_to_response('home_base.html',{'cartLength':cart_length})    visits = int(request.COOKIES.get('visits', '0'))    if 'last_visit' in request.COOKIES:        last_visit = request.COOKIES['last_visit']        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")        if (datetime.now() - last_visit_time).days > 0:            response.set_cookie('visits', visits + 1)            response.set_cookie('last_visit', datetime.now())    else:        response.set_cookie('last_visit', datetime.now())    return responsedef home(request):    products = ItemizedPreorder.objects.all().order_by('name')    pages = pagination(request, products, 21)    return render(request, 'preorders.html', {'items': pages[0], 'page_range': pages[1]})def info(request):    from django.core import serializers    product_id = request.GET.get('product_id')    data = {        "card": serializers.serialize("json", MtgDatabase.objects.filter(product_id=product_id))    }    return JsonResponse(data)def search(request):    template = 'preorders.html'    query = request.GET.get('q')    error = ''    if query:        results = ItemizedPreorder.objects.filter(Q(name__icontains=query))    else:        results = ItemizedPreorder.objects.all().order_by('name')    pages = pagination(request, results, 21)    '''prices = [3.0 for _ in range(len(results))]  # [query_dict[i.product_id]["market_price"] for i in results]    forms = [ProductForm(instance=i) for i in results]'''    context = {'items': pages[0], 'page_range': pages[1]}    return render(request, template, context)'''error = "{}".format(query)context = {'error': error}return render(request, template, context)'''def get_price(request):    response = {}    product_id = request.POST.get('productId')    try:        item = Product.objects.get(id=product_id)        response['price'] = item.price        response['success'] = True    except ObjectDoesNotExist:        response['error'] = "Item not found!"        response['success'] = False    return JsonResponse(response)def search_list(request):    template = 'search_result_list.html'    basics = ['plains', 'island', 'swamp', 'mountain', 'forest']    results = Product.objects.exclude(site='error').only('set_name','price').order_by('name')    error = ''    query = request.GET.get('q')    if query:        results_dict = {}        query = query.split('\n')        for each in query:            if len(each) > 1:                if each[0].isnumeric():                    each = each.replace('.', '')                    x = re.sub('[0-9]+', '', each.strip()).strip()                    if x[0].lower() == 'x':                        if x[1] == ' ':                            x = x.replace(x[0], '').strip()                    if x.strip().lower() not in basics:                        y = re.sub('[^0-9]', '', each.strip())                        if x not in results_dict:                            results_dict[x] = int(y)                        else:                            results_dict[x] += int(y)                else:                    if each[0].lower() == 'x':                        if each[1] == ' ':                            each = each.replace(each[0], '').strip()                    if each.strip().lower() not in basics:                        if each.strip().lower() not in results_dict:                            results_dict[each.strip()] = 1                        else:                            results_dict[each.strip()] += 1    else:        error = 'No query specified'    print(results_dict)    if query:        final_dict = {}        errors_in_query = []        for each in results_dict.keys():            r = results.filter(name=each.strip())            if not r.exists():                errors_in_query.append(each)            else:                for hit in r:                    final_dict[hit.id] = results_dict[each]        results = results.filter(            reduce(or_, (Q(name=itm.strip()) for itm in results_dict.keys()))        )        if request.GET.get('a') == 'express':            query_list = [] # To add name of objects as strings that have successfully been filtered, as to call a function on just one name            product_ids_tuple = [str(i.tcg_player_id) for i in results if i]            if len(product_ids_tuple) > 0:                query_dict = card_price(product_ids_tuple)            for each in results:                if each.name not in query_list: # Checks if the name of the object is not in in the query list                    query_list.append(each.name) # Adds just the name of the objects so there is just one of each name in query_list                try:                    each.price = query_dict[each.tcg_player_id]["market_price"]                    if each.price < 1.:                        each.price = price_for_rarity(each.rarity, each.price)                    each.save()                except KeyError:                    each.price = 1000                    each.save()            for each in query_list:                priced = results.filter(name=each).order_by('price').first() # Lowest price for each name in query_list                #p.sort(key=attrgetter('price'))                express_add_to_cart(request, priced.id, quantity=final_dict[priced.id])            if len(errors_in_query) > 0:                cart = Cart(request)                for each in errors_in_query:                    obj_error = results.create(name="Error for {}".format(each), site='error')                    obj_error.save()                    cart.add(obj_error, price = 0, set_name='No Results. Check your spelling.', quantity=1)            return redirect('cart')        elif request.GET.get('a') == 'list':            no_result = [i for i in errors_in_query]            some_context = {                'products': results,                'error': error,                'no_result': no_result,            }            return render(request, template, some_context)    elif not error:        error = 'Empty query'    some_context = {        'products': results,    }    return render(request, template, some_context)def express_add_to_cart(request, product_id, quantity=1):    products = get_object_or_404(Product, id=product_id)    cart = Cart(request)    cart.add(products, products.price, products.set_name, quantity)    return redirect('cart')def search_result(request):    tcg_price = 'Unavailable'    return render(request, 'search_result.html', {'tcg_price': tcg_price})def product_detail(request, product_id):    products = get_object_or_404(Product, id=product_id)    products.price = card_price_single(products.tcg_player_id, products.rarity)    products.save()    versions = Product.objects.filter(name=products.name)    return render(request, 'product_detail.html', {'products':products, 'versions':versions, 'price':products.price})def orders_view(request, product_info):    results = product_info.replace('+', ' ').replace('\n', '').split('\r')    print(results)    quantity = {i[1:].lower(): {'q': i[0]} for i in results if i != ''}    print(quantity)    results = [i[1:] for i in results if i != '']    products = Product.objects.filter(name__in=results).order_by('name')    q = [quantity[i.name.lower()]['q'] for i in products]    print(q)    order = zip(products, q)    return render(request, 'order_results.html', {'results': order})def get_cart(request):    cart = Cart(request)    length = cart.cart_length    sub_total = cart.total_price    return render(request, 'cart.html', {'cart': cart, 'length': length, 'sub_total': sub_total})def add_to_cart(request, product_id):    print(product_id)    quantity = request.POST.get('quantity')    # condition = request.POST.get('condition')    # language = request.POST.get('language')    products = get_object_or_404(ItemizedPreorder, id=product_id)    price = products.price    total = price * Decimal(quantity)    cart = Cart(request)    cart.add(product_id, products.name, price, products.expansion, condition='NM', language='English', total=total, quantity=quantity)    for each in cart:        print(each)    return redirect('cart')def remove_from_cart(request, product_id):    products = ItemizedPreorder.objects.get(id=product_id)    cart = Cart(request)    cart.remove(products)    return redirect('cart')def clear(request):    cart = Cart(request)    cart.clear()    return redirect('cart')def paypal_transaction(request, name, email):    if request:        data = ast.literal_eval(request.body.decode('utf-8'))        data = data['data']        print(data)        paypal_data = paypal.get_order(data['orderID'])        print(paypal_data)        order_info = paypal_data['purchase_units'][0]        payment_status = order_info['payments']['captures'][0]['status']        if payment_status == 'COMPLETED':            cart = Cart(request)            cart_data = [i for i in cart]            complete_order.apply_async(que='low_priority', args=(cart_data, name, email, data['orderID'], ))            cart.clear()            amount = order_info['amount']['value']            amount_currency_type = order_info['amount']['currency_code']            seller_email = order_info['payee']['email_address']            merchant_id = order_info['payee']['merchant_id']            shipping_name = order_info['shipping']['name']['full_name']            address_line_1 = order_info['shipping']['address']['address_line_1']            admin_area_2 = order_info['shipping']['address']['admin_area_2']            admin_area_1 = order_info['shipping']['address']['admin_area_1']            postal_code = order_info['shipping']['address']['postal_code']            country_code = order_info['shipping']['address']['country_code']            payment_id = order_info['payments']['captures'][0]['id']            paypal_fee = order_info['payments']['captures'][0]['seller_receivable_breakdown']['paypal_fee']['value']            net = order_info['payments']['captures'][0]['seller_receivable_breakdown']['net_amount']['value']            create_time = order_info['payments']['captures'][0]['create_time']            update_time = order_info['payments']['captures'][0]['update_time']            first_name = paypal_data['payer']['name']['given_name']            last_name = paypal_data['payer']['name']['surname']            payer_email = paypal_data['payer']['email_address']            payer_id = paypal_data['payer']['payer_id']            payer_country_code = paypal_data['payer']['address']['country_code']            paypal_record = PaypalOrder(                order_id=data['orderID'],                amount=amount,                amount_currency_type=amount_currency_type,                my_email=seller_email,                merchant_id=merchant_id,                shipping_name=shipping_name,                address_line_1=address_line_1,                admin_area_1=admin_area_1,                admin_area_2=admin_area_2,                postal_code=postal_code,                country_code=country_code,                payment_id=payment_id,                payment_status=payment_status,                paypal_fee=paypal_fee,                net=net,                create_time=create_time,                update_time=update_time,                first_name=first_name,                last_name=last_name,                customer_payment_email=payer_email,                customer_contact_email=email,                checkout_name=name,                customer_id=payer_id,                customer_country_code=payer_country_code,            )            paypal_record.save()        return JsonResponse({'success': 'True'})    else:        return JsonResponse({'success': 'False'})def payment(request):    name = request.POST.get('name')    email = request.POST.get('email')    notes = request.POST.get('notes')    cart = Cart(request)    total = cart.total_price    template = 'payment.html'    context = {        'total': total,        'name': name,        'email': email,    }    return render(request, template, context)def checkout(request):    cart = Cart(request)    sub_total = cart.total_price    length = len(cart)    title = ''    form = contactForm(request.POST or None)    confirm_message = None    '''paypal_dict = {        "business": "mtgfirststore-facilitator@gmail.com",        "amount": sub_total,        "item_name": 'mtg singles',        "invoice": "unique-invoice-id",        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),        "return": request.build_absolute_uri(reverse('home')),        "cancel_return": request.build_absolute_uri(reverse('home')),        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)    }    paypal_form = PayPalPaymentsForm(initial=paypal_dict)'''    if form.is_valid():        name = form.cleaned_data['name']        notes = form.cleaned_data['notes']        email = form.cleaned_data['email']        # send_order.apply_async(que='high_priority', args=(cart, name, notes, email))        title = 'Your order has been placed' \                'You will be contacted once we have checked availability and pricing for your list.' \                'Thank you for shopping with MTG First'        confirm_message = 'You will receive an email confirmation shortly'        form = None    return render(request, 'checkout.html', {'cart': cart, 'length': length,                                             'title': title, 'form': form, 'confirm_message': confirm_message, 'sub_total': sub_total})def supplies(request):    return render(request, 'supplies.html')def category(request, global_id):    supplies = Product.objects.filter(brand=global_id)    return render(request, global_id + '.html', {'supplies': supplies})def item(request, global_id):    supplies = Product.objects.filter(names=global_id)    return render(request, 'item-type.html', {'supplies': supplies})def sleeves(request):    supplies = Product.objects.filter(item_type='Sleeves')    pages = pagination(request, supplies, 20)    return render(request, 'sleeves.html', {'supplies': pages[0], 'page_range':pages[1]})def booster_packs(request):    supplies = Product.objects.filter(item_type='Booster_packs')    pages = pagination(request, supplies, 20)    return render(request, 'booster_packs,html.html', {'supplies': pages[0], 'page_range':pages[1]})def binders(request):    supplies = Product.objects.filter(item_type='Binders')    pages = pagination(request, supplies, 20)    return render(request, 'binders.html', {'supplies': pages[0], 'page_range':pages[1]})def deckboxes(request):    supplies = Product.objects.filter(item_type='Deckbox')    pages = pagination(request, supplies, 20)    return render(request, 'deckboxes.html', {'supplies': pages[0], 'page_range':pages[1]})def playmats_tubes(request):    supplies = Product.objects.filter(item_type='Playmats_tubes')    pages = pagination(request, supplies, 20)    return render(request, 'playmats-tubes.html', {'supplies': pages[0], 'page_range': pages[1]})def snacks_drinks(request):    supplies = Product.objects.filter(item_type='Snacks_drinks')    pages = pagination(request, supplies, 20)    return render(request, 'snacks-drinks.html', {'supplies': pages[0], 'page_range': pages[1]})def preorders(request):    products = ItemizedPreorder.objects.all().order_by('name')    pages = pagination(request, products, 21)    return render(request, 'preorders.html', {'items': pages[0], 'page_range': pages[1]})def thanks(request):    return render(request, 'thank-you.html')