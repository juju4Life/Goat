from django.core.management.base import BaseCommand
from engine.tcgplayer_api import TcgPlayerApi
from my_customs.decorators import report_error
from engine.tcg_manifest import Manifest
from orders.models import GroupName, Inventory
from tcg.price_alogrithm import *
from time import time

api = TcgPlayerApi()
M = Manifest()


class Command(BaseCommand):
    def handle(self, **options):
        start = time()
        # Cards in database as True or False for printing type
        foil_map = {
            True: 'Foil',
            False: 'Normal',
        }

        # Maps condition for cards that have other information attached to the condition field
        def condition_map(cond):
            cond = cond.lower()
            lp = 'lightly played'
            nm = 'near mint'
            mp = 'moderately played'
            hp = 'heavily played'
            dmg = 'damaged'
            if lp in cond:
                cond = lp
            elif nm in cond:
                cond = nm
            elif mp in cond:
                cond = mp
            elif hp in cond:
                cond = hp
            elif dmg in cond:
                cond = dmg
            return cond

        # Query all groups labeled Magic the Gathering
        groups = GroupName.objects.filter(category='Magic the Gathering')

        # Query through all groups. For each, if a filtered result in the Inventory exisits, prepare var to loop over Inventory filtered list
        for index, group in enumerate(groups):
            inventory = Inventory.objects.filter(expansion=group.group_name)

            # Get pricing data for entire group
            if inventory:
                pricing_data = api.price_by_group_id(str(group.group_id))
                print(group.group_name, index)

                # Create dictionary with all pricing results mapped to product Id
                if pricing_data['success']:
                    pricing_data = pricing_data['results']
                    d = {
                        i['productId']: {
                            'Foil': {
                                'low': 0,
                                'mid': 0,
                                'market': 0,
                                'direct': 0,
                            },
                            'Normal': {
                                'low': 0,
                                'mid': 0,
                                'market': 0,
                                'direct': 0,
                            },
                        } for i in pricing_data
                    }

                    for price in pricing_data:
                        sub_type = price['subTypeName']
                        product_id = price['productId']
                        low = price['lowPrice']
                        market = price['marketPrice']
                        mid = price['midPrice']
                        direct = price['directLowPrice']

                        d[product_id][sub_type]['low'] = low
                        d[product_id][sub_type]['market'] = market
                        d[product_id][sub_type]['mid'] = mid
                        d[product_id][sub_type]['direct'] = direct

                    # Loop through each item in Inventory, if quantity > 0  and ignore Sealed product
                    for item in inventory:
                        if item.quantity > 0:
                            if item.condition != 'Unopened':

                                # API call using each sku for product_id
                                sku = item.sku
                                product_id = api.card_info_by_sku(sku)['results'][0]['productId']

                                # Grab pricing data from dictionary using product id
                                price_lib = d[product_id]

                                # Run pricing algorithm base on foiling an language
                                is_foil = foil_map[bool(item.printing)]
                                if is_foil == 'Normal':
                                    price_lib = price_lib['Normal']
                                    if item.language == 'English':
                                        condition = item.condition
                                        updated_price = price_algorithm(
                                            condition=condition,
                                            market=price_lib['market'],
                                            direct=price_lib['direct'],
                                            mid=price_lib['mid'],
                                            low=price_lib['low'],
                                        )
                                        item.price = updated_price

                                    else:
                                        condition = condition_map(item.condition)
                                        updated_price = price_foreign(
                                            language=item.language,
                                            condition=condition,
                                            market=price_lib['market'],
                                            direct=price_lib['direct'],
                                            mid=price_lib['mid'],
                                            low=price_lib['low'],
                                        )
                                        item.price = updated_price

                                elif is_foil == 'Foil':
                                    price_lib = price_lib['Foil']
                                    if item.language == 'English':
                                        condition = condition_map(item.condition)
                                        updated_price = price_foils(
                                            condition=condition,
                                            market=price_lib['market'],
                                            direct=price_lib['direct'],
                                            mid=price_lib['mid'],
                                            low=price_lib['low'],
                                        )
                                        item.price = updated_price
                                    else:
                                        # Foil Foreign
                                        pass

                                else:
                                    raise Exception(f'Card {item.name} {item.expansion} not labeled foil or non-foil, {item.printing}')
                                item.save()

        stop = time()

        elapsed = stop - start

        print(f"Function finished in {elapsed}")





