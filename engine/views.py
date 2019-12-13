from django.shortcuts import render, redirect, HttpResponseRedirectfrom django.http import JsonResponsefrom django.shortcuts import get_object_or_404, render_to_responsefrom django.views.decorators.cache import cache_pagefrom .models import MTGfrom datetime import datetimefrom .cart import Cartfrom .forms import contactForm, ProductFormfrom django.db.models import Qfrom .config import paginationfrom engine.tcgplayer_api import TcgPlayerApifrom functools import reducefrom operator import or_from customer.models import ItemizedPreorderimport refrom decimal import Decimalfrom ppal.paypal_api import PaypalApifrom ppal.models import PaypalOrderimport astfrom .tasks import complete_orderfrom django.core.mail import send_mailimport randomfrom rest_framework.views import APIViewfrom rest_framework.response import Responsefrom buylist.models import HotListfrom scryfall_api import get_imagetcg = TcgPlayerApi('first')paypal = PaypalApi()def home_base(request):    cart = Cart(request)    cart_length = cart.cart_length    response = render_to_response('home_base.html', {'cartLength': cart_length})    visits = int(request.COOKIES.get('visits', '0'))    if 'last_visit' in request.COOKIES:        last_visit = request.COOKIES['last_visit']        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")        if (datetime.now() - last_visit_time).days > 0:            response.set_cookie('visits', visits + 1)            response.set_cookie('last_visit', datetime.now())    else:        response.set_cookie('last_visit', datetime.now())    return responsedef home(request):    return render(request, 'home.html', {})class PopularCardsGallery(APIView):    authentication_classes = []    permission_classes = []    def get(self, request, format=None):        cards = HotList.objects.all()        data = {           'cards': [[i.name, i.expansion, i.price, i.image] for i in cards]        }        return Response(data)class CardDatabase(APIView):    authentication_classes = []    permission_classes = []    # @cache_page(60 * 20)    def get(self, request, format=None):        from django.forms.models import model_to_dict        cards = [model_to_dict(i) for i in MTG.objects.filter(condition='Near Mint')]        data = {           'products': cards        }        return Response(data)def search(request):    template = 'search_result.html'    query = request.GET.get('q')    hotlist = HotList.objects.all()    error = ''    if query:        results = MTG.objects.filter(Q(product_name__icontains=query)).filter(condition='Near Mint')    else:        # results = MTG.objects.all().order_by('product_name')        error = 'No data'        results = []    pages = pagination(request, results, 21)    if results:        related_products = tcg.get_related_products(results[0].product_id)        if related_products['success']:            card = [{'name': i['purchasedProductName'], 'image': get_image(i['purchasedStoreProductId'])} for i in related_products['results'][0:6]]        else:            card = None    '''prices = [3.0 for _ in range(len(results))]  # [query_dict[i.product_id]["market_price"] for i in results]    forms = [ProductForm(instance=i) for i in results]'''    context = {'items': pages[0], 'page_range': pages[1], 'error': error, 'hotlist': hotlist, 'related_products': card}    return render(request, template, context)'''error = "{}".format(query)context = {'error': error}return render(request, template, context)'''def search_list(request):    template = 'search_result_list.html'    basics = ['plains', 'island', 'swamp', 'mountain', 'forest']    results = object.objects.exclude(site='error').only('set_name', 'price').order_by('name')    error = ''    query = request.GET.get('q')    if query:        results_dict = {}        query = query.split('\n')        for each in query:            if len(each) > 1:                if each[0].isnumeric():                    each = each.replace('.', '')                    x = re.sub('[0-9]+', '', each.strip()).strip()                    if x[0].lower() == 'x':                        if x[1] == ' ':                            x = x.replace(x[0], '').strip()                    if x.strip().lower() not in basics:                        y = re.sub('[^0-9]', '', each.strip())                        if x not in results_dict:                            results_dict[x] = int(y)                        else:                            results_dict[x] += int(y)                else:                    if each[0].lower() == 'x':                        if each[1] == ' ':                            each = each.replace(each[0], '').strip()                    if each.strip().lower() not in basics:                        if each.strip().lower() not in results_dict:                            results_dict[each.strip()] = 1                        else:                            results_dict[each.strip()] += 1    else:        error = 'No query specified'    print(results_dict)    if query:        final_dict = {}        errors_in_query = []        for each in results_dict.keys():            r = results.filter(name=each.strip())            if not r.exists():                errors_in_query.append(each)            else:                for hit in r:                    final_dict[hit.id] = results_dict[each]        results = results.filter(            reduce(or_, (Q(name=itm.strip()) for itm in results_dict.keys()))        )        if request.GET.get('a') == 'express':            query_list = []  # To add name of objects as strings that have successfully been filtered, as to call a function on just one name            product_ids_tuple = [str(i.tcg_player_id) for i in results if i]            if len(product_ids_tuple) > 0:                # query_dict = card_price(product_ids_tuple)                query_dict = ''            for each in results:                if each.name not in query_list: # Checks if the name of the object is not in in the query list                    query_list.append(each.name) # Adds just the name of the objects so there is just one of each name in query_list                try:                    each.price = query_dict[each.tcg_player_id]["market_price"]                    if each.price < 1.:                        each.price = ''                    each.save()                except KeyError:                    each.price = 1000                    each.save()            for each in query_list:                priced = results.filter(name=each).order_by('price').first() # Lowest price for each name in query_list                #p.sort(key=attrgetter('price'))                # express_add_to_cart(request, priced.id, quantity=final_dict[priced.id])            if len(errors_in_query) > 0:                cart = Cart(request)                for each in errors_in_query:                    obj_error = results.create(name="Error for {}".format(each), site='error')                    obj_error.save()                    cart.add(obj_error, price=0, set_name='No Results. Check your spelling.', quantity=1)            return redirect('cart')        elif request.GET.get('a') == 'list':            no_result = [i for i in errors_in_query]            some_context = {                'products': results,                'error': error,                'no_result': no_result,            }            return render(request, template, some_context)    elif not error:        error = 'Empty query'    some_context = {        'products': results,    }    return render(request, template, some_context)def search_result(request):    tcg_price = 'Unavailable'    return render(request, 'search_result.html', {'tcg_price': tcg_price})def product_detail(request, product_id):    product = MTG.objects.filter(product_id=product_id).filter(condition='Near Mint').filter(foil=False)    # versions = object.objects.filter(name=products)    return render(request, 'product_detail.html', {'product': product[0]})def orders_view(request, product_info):    results = product_info.replace('+', ' ').replace('\n', '').split('\r')    print(results)    quantity = {i[1:].lower(): {'q': i[0]} for i in results if i != ''}    print(quantity)    results = [i[1:] for i in results if i != '']    products = object.objects.filter(name__in=results).order_by('name')    q = [quantity[i.name.lower()]['q'] for i in products]    print(q)    order = zip(products, q)    return render(request, 'order_results.html', {'results': order})def get_cart(request):    cart = Cart(request)    length = cart.cart_length    sub_total = cart.total_price    return render(request, 'cart.html', {'cart': cart, 'length': length, 'sub_total': sub_total})def add_to_cart(request, product_id):    print(product_id)    quantity = request.POST.get('quantity')    # condition = request.POST.get('condition')    # language = request.POST.get('language')    products = get_object_or_404(ItemizedPreorder, id=product_id)    price = products.price    total = price * Decimal(quantity)    cart = Cart(request)    cart.add(product_id, products.name, price, products.expansion, condition='NM', language='English', total=total, quantity=quantity)    return redirect('cart')def remove_from_cart(request, product_id):    products = ItemizedPreorder.objects.get(id=product_id)    cart = Cart(request)    cart.remove(products)    return redirect('cart')def clear(request):    cart = Cart(request)    cart.clear()    return redirect('cart')def paypal_transaction(request, name, email):    if request:        data = ast.literal_eval(request.body.decode('utf-8'))        data = data['data']        paypal_data = paypal.get_order(data['orderID'])        if paypal_data.get('error') == 'invalid_token':            paypal.get_access_token()            paypal_data = paypal.get_order(data['orderID'])        order_id = data.get('orderID', random.sample(range(10000000, 99999999), 1))        order_info = paypal_data['purchase_units'][0]        payment_status = order_info['payments']['captures'][0]['status']        if payment_status == 'COMPLETED':            cart = Cart(request)            cart_data = [i for i in cart]            complete_order.apply_async(que='low_priority', args=(cart_data, name, email, order_id, ))            cart.clear()            amount = order_info['amount']['value']            amount_currency_type = order_info['amount']['currency_code']            seller_email = order_info['payee']['email_address']            merchant_id = order_info['payee']['merchant_id']            shipping_name = order_info['shipping']['name']['full_name']            address_line_1 = order_info['shipping']['address']['address_line_1']            admin_area_2 = order_info['shipping']['address']['admin_area_2']            admin_area_1 = order_info['shipping']['address']['admin_area_1']            postal_code = order_info['shipping']['address']['postal_code']            country_code = order_info['shipping']['address']['country_code']            payment_id = order_info['payments']['captures'][0]['id']            paypal_fee = order_info['payments']['captures'][0]['seller_receivable_breakdown']['paypal_fee']['value']            net = order_info['payments']['captures'][0]['seller_receivable_breakdown']['net_amount']['value']            create_time = order_info['payments']['captures'][0]['create_time']            update_time = order_info['payments']['captures'][0]['update_time']            first_name = paypal_data['payer']['name']['given_name']            last_name = paypal_data['payer']['name']['surname']            payer_email = paypal_data['payer']['email_address']            payer_id = paypal_data['payer']['payer_id']            payer_country_code = paypal_data['payer']['address']['country_code']            paypal_record = PaypalOrder(                order_id=order_id,                amount=amount,                amount_currency_type=amount_currency_type,                my_email=seller_email,                merchant_id=merchant_id,                shipping_name=shipping_name,                address_line_1=address_line_1,                admin_area_1=admin_area_1,                admin_area_2=admin_area_2,                postal_code=postal_code,                country_code=country_code,                payment_id=payment_id,                payment_status=payment_status,                paypal_fee=paypal_fee,                net=net,                create_time=create_time,                update_time=update_time,                first_name=first_name,                last_name=last_name,                customer_payment_email=payer_email,                customer_contact_email=email,                checkout_name=name,                customer_id=payer_id,                customer_country_code=payer_country_code,            )            paypal_record.save()            grand_total = sum([float(i['total']) for i in cart_data])            new_order = [                f"{i['quantity']} {i['name']}, ({i['set_name']}) ${i['price']} | Total: ${i['total']}\n"                for i in cart_data            ]            subject = 'Order Received'            message = f"Order #{order_id}\n\n" \                f"{''.join(new_order)}\n" \                f"Grand Total: {grand_total}"            recipient_list = ['sales@mtgfirst.com']            from_mail = 'MTGFirst'            send_mail(subject=subject, message=message, recipient_list=recipient_list, from_email=from_mail)        return JsonResponse({"success": 'True'})    else:        return JsonResponse({'success': 'False'})def order_confirmation(request):    events = Events.objects.all()    template = 'order_complete.html'    context = {'events': events}    return render(request, template, context)def payment(request):    name = request.POST.get('name')    email = request.POST.get('email')    cart = Cart(request)    total = cart.total_price    template = 'payment.html'    context = {        'total': total,        'name': name,        'email': email,    }    return render(request, template, context)def checkout(request):    cart = Cart(request)    sub_total = cart.total_price    length = len(cart)    title = ''    form = contactForm(request.POST or None)    confirm_message = None    '''paypal_dict = {        "business": "mtgfirststore-facilitator@gmail.com",        "amount": sub_total,        "item_name": 'mtg singles',        "invoice": "unique-invoice-id",        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),        "return": request.build_absolute_uri(reverse('home')),        "cancel_return": request.build_absolute_uri(reverse('home')),        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)    }    paypal_form = PayPalPaymentsForm(initial=paypal_dict)'''    if form.is_valid():        name = form.cleaned_data['name']        notes = form.cleaned_data['notes']        email = form.cleaned_data['email']        # send_order.apply_async(que='high_priority', args=(cart, name, notes, email))        title = 'Your order has been placed' \                'You will be contacted once we have checked availability and pricing for your list.' \                'Thank you for shopping with MTG First'        confirm_message = 'You will receive an email confirmation shortly'        form = None    return render(request, 'checkout.html', {'cart': cart, 'length': length,                                             'title': title, 'form': form, 'confirm_message': confirm_message, 'sub_total': sub_total})def thanks(request):    return render(request, 'thank-you.html')