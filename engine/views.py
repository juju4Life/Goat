from django.shortcuts import render, redirectfrom django.http import JsonResponsefrom decimal import Decimalfrom django.shortcuts import get_object_or_404, render_to_responsefrom datetime import datetimefrom .cart import Cartfrom .forms import contactFormfrom django.conf import settingsfrom django.core.mail import send_mailfrom django.db.models import Qfrom .config import paginationfrom .models import Productfrom functools import reducefrom operator import or_from .tcgplayer import card_price, search_inventory, price_for_rarity, card_price_single, TcgPlayerApiimport refrom customer.models import OrderRequesttcg = TcgPlayerApi()def home(request):    cart = Cart(request)    cart_length = cart.cart_length    response = render_to_response('home.html',{'cartLength':cart_length})    visits = int(request.COOKIES.get('visits', '0'))    if 'last_visit' in request.COOKIES:        last_visit = request.COOKIES['last_visit']        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")        if (datetime.now() - last_visit_time).days > 0:            response.set_cookie('visits', visits + 1)            response.set_cookie('last_visit', datetime.now())    else:        response.set_cookie('last_visit', datetime.now())    return responsedef search(request):    template = 'search_result.html'    query = request.GET.get('q')    error = ''    if query:        results = Product.objects.exclude(site='error').filter(Q(name__icontains=query))        if len(results) > 0:            product_ids_tuple = [str(i.tcg_player_id) for i in results]            if len(product_ids_tuple) > 0:                query_dict = card_price(product_ids_tuple)            for each in results:                try:                    each.price = query_dict[each.tcg_player_id]["market_price"]                    each.price = price_for_rarity(each.rarity, each.price)                    each.save()                except KeyError:                    each.price = 1000                    each.save()            pages = pagination(request, results, 20)            context = {'products': pages[0], 'page_range': pages[1], 'error': error}            return render(request, template, context)        else:            error = "{}".format(query)            context = {'error': error}            return render(request, template, context)    else:        return redirect('home')def get_price(request):    response = {}    product_id = request.POST.get('productId')    try:        item = Product.objects.get(id=product_id)        response['price'] = item.price        response['success'] = True    except ObjectDoesNotExist:        response['error'] = "Item not found!"        response['success'] = False    return JsonResponse(response)def search_list(request):    template = 'search_result_list.html'    basics = ['plains', 'island', 'swamp', 'mountain', 'forest']    results = Product.objects.exclude(site='error').only('set_name','price').order_by('name')    error = ''    query = request.GET.get('q')    if query:        results_dict = {}        query = query.split('\n')        for each in query:            if len(each) > 1:                if each[0].isnumeric():                    each = each.replace('.', '')                    x = re.sub('[0-9]+', '', each.strip()).strip()                    if x[0].lower() == 'x':                        if x[1] == ' ':                            x = x.replace(x[0], '').strip()                    if x.strip().lower() not in basics:                        y = re.sub('[^0-9]', '', each.strip())                        if x not in results_dict:                            results_dict[x] = int(y)                        else:                            results_dict[x] += int(y)                else:                    if each[0].lower() == 'x':                        if each[1] == ' ':                            each = each.replace(each[0], '').strip()                    if each.strip().lower() not in basics:                        if each.strip().lower() not in results_dict:                            results_dict[each.strip()] = 1                        else:                            results_dict[each.strip()] += 1    else:        error = 'No query specified'    print(results_dict)    if query:        final_dict = {}        errors_in_query = []        for each in results_dict.keys():            r = results.filter(name=each.strip())            if not r.exists():                errors_in_query.append(each)            else:                for hit in r:                    final_dict[hit.id] = results_dict[each]        results = results.filter(            reduce(or_, (Q(name=itm.strip()) for itm in results_dict.keys()))        )        if request.GET.get('a') == 'express':            query_list = [] # To add name of objects as strings that have successfully been filtered, as to call a function on just one name            product_ids_tuple = [str(i.tcg_player_id) for i in results if i]            if len(product_ids_tuple) > 0:                query_dict = card_price(product_ids_tuple)            for each in results:                if each.name not in query_list: # Checks if the name of the object is not in in the query list                    query_list.append(each.name) # Adds just the name of the objects so there is just one of each name in query_list                try:                    each.price = query_dict[each.tcg_player_id]["market_price"]                    if each.price < 1.:                        each.price = price_for_rarity(each.rarity, each.price)                    each.save()                except KeyError:                    each.price = 1000                    each.save()            for each in query_list:                priced = results.filter(name=each).order_by('price').first() # Lowest price for each name in query_list                #p.sort(key=attrgetter('price'))                express_add_to_cart(request, priced.id, quantity=final_dict[priced.id])            if len(errors_in_query) > 0:                cart = Cart(request)                for each in errors_in_query:                    obj_error = results.create(name="Error for {}".format(each), site='error')                    obj_error.save()                    cart.add(obj_error, price = 0, set_name='No Results. Check your spelling.', quantity=1)            return redirect('cart')        elif request.GET.get('a') == 'list':            no_result = [i for i in errors_in_query]            some_context = {                'products': results,                'error': error,                'no_result': no_result,            }            return render(request, template, some_context)    elif not error:        error = 'Empty query'    some_context = {        'products': results,    }    return render(request, template, some_context)def express_add_to_cart(request, product_id, quantity=1):    products = get_object_or_404(Product, id=product_id)    cart = Cart(request)    cart.add(products, products.price, products.set_name, quantity)    return redirect('cart')def search_result(request):    tcg_price = 'Unavailable'    return render(request, 'search_result.html', {'tcg_price': tcg_price})def product_detail(request, product_id):    products = get_object_or_404(Product, id=product_id)    products.price = card_price_single(products.tcg_player_id, products.rarity)    products.save()    versions = Product.objects.filter(name=products.name)    return render(request, 'product_detail.html', {'products':products, 'versions':versions, 'price':products.price})def orders_view(request, product_info):    results = product_info.replace('+', ' ').replace('\n', '').split('\r')    print(results)    quantity = {i[1:].lower(): {'q': i[0]} for i in results if i != ''}    print(quantity)    results = [i[1:] for i in results if i != '']    products = Product.objects.filter(name__in=results).order_by('name')    q = [quantity[i.name.lower()]['q'] for i in products]    print(q)    order = zip(products, q)    return render(request, 'order_results.html', {'results':order})def get_cart(request):    cart = Cart(request)    length = cart.cart_length    sub_total = cart.total_price    total = [i['quantity'] * i['price'] for i in cart]    cart_data = zip(cart, total)    return render(request, 'cart.html', {'cart':cart_data, 'length':length, 'sub_total':sub_total})def add_to_cart(request, product_id):    quantity = request.POST.get('quantity')    products = get_object_or_404(Product, id=product_id)    if products.site == 'database':        products.price = card_price_single(products.tcg_player_id, products.rarity)        products.save()    else:        products.price = Decimal(products.price)        products.save()    cart = Cart(request)    cart.add(products, products.price, products.set_name, quantity)    return redirect('cart')def remove_from_cart(request, product_id):    products = Product.objects.get(id=product_id)    cart = Cart(request)    cart.remove(products)    return redirect('cart')def clear(request):    cart = Cart(request)    cart.clear()    return redirect('cart')from customer.tasks import send_orderdef checkout(request):    cart = Cart(request)    cart_dict = []    for each in cart:        if each['product'].site != 'error':            product = each['product']            d = {                'name': product.name,                'set_name': each['set_name'],                'quantity': each['quantity'],                'price': each['price'],                'site': product.site,                'tcg_id': product.tcg_player_id,                'rarity': product.rarity            }            cart_dict.append(d)    total = [i['quantity'] * i['price'] for i in cart]    cart_data = zip(cart, total)    sub_total = cart.total_price    length = len(cart)    for each in cart:        if each['product'].site == 'error':            length -= 1    title = ''    form = contactForm(request.POST or None)    confirm_message = None    if form.is_valid():        name = form.cleaned_data['name']        notes = form.cleaned_data['notes']        email = form.cleaned_data['email']        phone_number = form.cleaned_data['phone_number']        contact_type = form.cleaned_data['contact_type']        send_order.apply_async(que='high_priority', args=(cart_dict, name, notes, email, phone_number, contact_type,))        title = 'Your order has been placed' \                'You will be contacted once we have checked availability and pricing for your list.' \                'Thank you for shopping with MTG First'        confirm_message = 'You will receive an email confirmation shortly'        form = None    return render(request, 'checkout.html', {'cart': cart_data, 'length': length,                                             'title': title, 'form': form, 'confirm_message': confirm_message, 'sub_total':sub_total})def supplies(request):    return render(request, 'supplies.html')def category(request, global_id):    supplies = Product.objects.filter(brand=global_id)    return render(request, global_id + '.html', {'supplies': supplies})def item(request, global_id):    supplies = Product.objects.filter(names=global_id)    return render(request, 'item-type.html', {'supplies': supplies})def expansion(request, set_name):    set_library = {'0': '15th Anniversary', '1': 'Aether Revolt', '2': 'Alara Reborn', '3': 'Alliances',                   '4': 'Amonkhet',                   '5': 'Anthologies', '6': 'Antiquities', '7': 'Apocalypse', '8': 'Arabian Nights', '9': 'Archenemy',                   '10': 'Archenemy: Nicol Bolas', '11': 'Arena League', '12': 'Asia Pacific Land Program',                   '13': 'Avacyn Restored',                   '14': 'Battle Royale Box Set', '15': 'Battle for Zendikar', '16': 'Beatdown Box Set',                   '17': 'Betrayers of Kamigawa', '18': 'Born of the Gods', '19': 'Celebration',                   '20': 'Champions of Kamigawa',                   '21': 'Champs and States', '22': 'Chronicles', '23': 'Classic Sixth Edition', '24': 'Coldsnap',                   '25': 'Coldsnap Theme Deck Reprints', '26': "Collector's Edition", '27': 'Commander 2013',                   '28': 'Commander 2014',                   '29': 'Commander 2015', '30': 'Commander 2016', '31': 'Commander 2017', '32': 'Commander Anthology',                   '33': "Commander's Arsenal", '34': 'Conflux', '35': 'Conspiracy: Take the Crown',                   '36': 'Dark Ascension',                   '37': 'Darksteel', '38': 'Deckmasters', '39': 'Dissension', '40': 'Dominaria', '41': 'Dragon Con',                   '42': "Dragon's Maze", '43': 'Dragons of Tarkir', '44': 'Duel Decks Anthology, Divine vs. Demonic',                   '45': 'Duel Decks Anthology, Elves vs. Goblins', '46': 'Duel Decks Anthology, Garruk vs. Liliana',                   '47': 'Duel Decks Anthology, Jace vs. Chandra', '48': 'Duel Decks: Ajani vs. Nicol Bolas',                   '49': 'Duel Decks: Blessed vs. Cursed', '50': 'Duel Decks: Divine vs. Demonic',                   '51': 'Duel Decks: Elspeth vs. Kiora', '52': 'Duel Decks: Elspeth vs. Tezzeret',                   '53': 'Duel Decks: Elves vs. Goblins', '54': 'Duel Decks: Elves vs. Inventors',                   '55': 'Duel Decks: Garruk vs. Liliana', '56': 'Duel Decks: Heroes vs. Monsters',                   '57': 'Duel Decks: Izzet vs. Golgari', '58': 'Duel Decks: Jace vs. Chandra',                   '59': 'Duel Decks: Jace vs. Vraska',                   '60': 'Duel Decks: Knights vs. Dragons', '61': 'Duel Decks: Merfolk vs. Goblins',                   '62': 'Duel Decks: Mind vs. Might', '63': 'Duel Decks: Nissa vs. Ob Nixilis',                   '64': 'Duel Decks: Phyrexia vs. the Coalition', '65': 'Duel Decks: Sorin vs. Tibalt',                   '66': 'Duel Decks: Speed vs. Cunning', '67': 'Duel Decks: Venser vs. Koth',                   '68': 'Duel Decks: Zendikar vs. Eldrazi', '69': 'Duels of the Planeswalkers', '70': '8th Edition',                   '71': 'Eldritch Moon', '72': 'Eternal Masters', '73': 'European Land Program', '74': 'Eventide',                   '75': 'Exodus',                   '76': 'Explorers of Ixalan', '77': 'Fallen Empires', '78': 'Fate Reforged',                   '79': 'Fate Reforged Clash Pack',                   '80': 'Fifth Dawn', '81': 'Fifth Edition', '82': 'Fourth Edition', '83': 'Friday Night Magic',                   '84': 'From the Vault: Angels', '85': 'From the Vault: Annihilation',                   '86': 'From the Vault: Dragons',                   '87': 'From the Vault: Exiled', '88': 'From the Vault: Legends', '89': 'From the Vault: Lore',                   '90': 'From the Vault: Realms', '91': 'From the Vault: Relics', '92': 'From the Vault: Transform',                   '93': 'From the Vault: Twenty', '94': 'Future Sight', '95': 'Gatecrash', '96': 'Gateway',                   '97': 'Grand Prix',                   '98': 'Guildpact', '99': 'Guru', '100': 'Happy Holidays', '101': 'Homelands',                   '102': 'Hour of Devastation',                   '103': 'Ice Age', '104': 'Iconic Masters', '105': 'Innistrad',                   '106': "International Collector's Edition",                   '107': 'Introductory Two-Player Set', '108': 'Invasion', '109': 'Ixalan', '110': 'Journey into Nyx',                   '111': 'Judge Gift Program', '112': 'Judgment', '113': 'Kaladesh', '114': 'Khans of Tarkir',                   '115': 'Launch Parties', '116': 'Legend Membership', '117': 'Legends', '118': 'Legions',                   '119': 'Limited Edition Alpha', '120': 'Limited Edition Beta', '121': 'Lorwyn', '122': 'Magic 2010 (M10)',                   '123': 'Magic 2011 (M11)', '124': 'Magic 2012 (M12)', '125': 'Magic 2013 (M13)', '126': 'Magic 2014 (M14)',                   '127': 'Magic 2015 Clash Pack', '128': 'Magic 2015 (M15)', '129': 'Magic Game Day',                   '130': 'Magic Origins',                   '131': 'Magic Origins Clash Pack', '132': 'Magic Player Rewards',                   '133': 'Commander',                   '134': 'Conspiracy', '135': 'Masterpiece Series: Amonkhet Invocations',                   '136': 'Masterpiece Series: Kaladesh Inventions', '137': 'Masters 25', '138': 'Masters Edition',                   '139': 'Masters Edition II', '140': 'Masters Edition III', '141': 'Masters Edition IV',                   '142': 'Media Inserts',                   '143': 'Mercadian Masques', '144': 'Mirage', '145': 'Mirrodin', '146': 'Mirrodin Besieged',                   '147': 'Magic Modern Event Deck', '148': 'Modern Masters', '149': 'Modern Masters 2015',                   '150': 'Modern Masters 2017', '151': 'Morningtide', '152': 'Multiverse Gift Box',                   '153': 'Nemesis',                   '154': 'New Phyrexia', '155': '9th Edition', '156': 'Oath of the Gatewatch', '157': 'Odyssey',                   '158': 'Onslaught', '159': 'Planar Chaos', '160': 'Planechase', '161': 'Planechase 2012',                   '162': 'Planechase Anthology', '163': 'Planeshift', '164': 'Portal', '165': 'Portal Demo Game',                   '166': 'Portal Second Age', '167': 'Portal Three Kingdoms',                   '168': 'Premium Deck Series: Fire and Lightning',                   '169': 'Premium Deck Series: Graveborn', '170': 'Premium Deck Series: Slivers',                   '171': 'Prerelease Events',                   '172': 'Pro Tour', '173': 'Prophecy', '174': 'Ravnica', '175': 'Release Events',                   '176': 'Return to Ravnica', '177': 'Revised Edition', '178': 'Rise of the Eldrazi',                   '179': 'Rivals Quick Start Set', '180': 'Rivals of Ixalan', '181': 'Saviors of Kamigawa',                   '182': 'Scars of Mirrodin', '183': 'Scourge', '184': '7th Edition', '185': 'Shadowmoor',                   '186': 'Shadows over Innistrad', '187': 'Shards of Alara', '188': 'Starter 1999',                   '189': 'Starter 2000',                   '190': 'Stronghold', '191': 'Summer of Magic', '192': 'Super Series', '193': 'Tempest',                   '194': 'Tempest Remastered', '195': '10th Edition', '196': 'The Dark', '197': 'Theros',                   '198': 'Time Spiral',                   '199': 'Timeshifted', '200': 'Torment', '201': 'Two-Headed Giant Tournament',                   '202': "Ugin's Fate promos", '203': 'Unglued', '204': 'Unhinged', '205': 'Unlimited Edition',                   '206': 'Unstable',                   '207': "Urza's Destiny", '208': "Urza's Legacy", '209': "Urza's Saga", '210': 'Vanguard',                   '211': 'Vintage Masters',                   '212': 'Visions', '213': 'Weatherlight', '214': 'Welcome Deck 2016', '215': 'Welcome Deck 2017',                   '216': 'Wizards Play Network', '217': 'Wizards of the Coast Online Store',                   '218': 'World Magic Cup Qualifiers',                   '219': 'Worlds', '220': 'Worldwake', '221': 'Zendikar', '222': 'Zendikar Expeditions',                   '223': 'Battlebond', '224': 'Core Set 2019', '225': 'Commander Anthology Volume II',                   '226': 'Signature Spellbook: Jace'                   }    products = Product.objects.filter(set_name=set_library[set_name])    pages = pagination(request, products, 100)    return render(request, 'expansions.html', {'items':pages[0],'page_range':pages[1]})def sleeves(request):    supplies = Product.objects.filter(item_type='Sleeves')    pages = pagination(request, supplies, 20)    return render(request, 'sleeves.html', {'supplies': pages[0], 'page_range':pages[1]})def booster_packs(request):    supplies = Product.objects.filter(item_type='Booster_packs')    pages = pagination(request, supplies, 20)    return render(request, 'booster_packs,html.html', {'supplies': pages[0], 'page_range':pages[1]})def binders(request):    supplies = Product.objects.filter(item_type='Binders')    pages = pagination(request, supplies, 20)    return render(request, 'binders.html', {'supplies': pages[0], 'page_range':pages[1]})def deckboxes(request):    supplies = Product.objects.filter(item_type='Deckbox')    pages = pagination(request, supplies, 20)    return render(request, 'deckboxes.html', {'supplies': pages[0], 'page_range':pages[1]})def playmats_tubes(request):    supplies = Product.objects.filter(item_type='Playmats_tubes')    pages = pagination(request, supplies, 20)    return render(request, 'playmats-tubes.html', {'supplies': pages[0], 'page_range':pages[1]})def snacks_drinks(request):    supplies = Product.objects.filter(item_type='Snacks_drinks')    pages = pagination(request, supplies, 20)    return render(request, 'snacks-drinks.html', {'supplies': pages[0], 'page_range':pages[1]})def preorders(request):    supplies = Product.objects.filter(site='Preorders')    pages = pagination(request, supplies, 20)    return render(request, 'preorders.html', {'supplies': pages[0], 'page_range':pages[1]})def thanks(request):    return render(request, 'thank-you.html')