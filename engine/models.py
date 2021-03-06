from datetime import datetime

from django.db import models
import pytz


class BasicCardInfo(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='name', db_index=True)
    expansion = models.CharField(max_length=255, default='', db_index=True)
    product_id = models.CharField(max_length=30, default='')
    normal_clean_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    normal_clean_stock = models.IntegerField(default=0)
    normal_played_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    normal_played_stock = models.IntegerField(default=0)
    normal_heavily_played_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    normal_heavily_played_stock = models.IntegerField(default=0)
    foil_clean_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    foil_clean_stock = models.IntegerField(default=0)
    foil_played_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    foil_played_stock = models.IntegerField(default=0)
    foil_heavily_played_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    foil_heavily_played_stock = models.IntegerField(default=0)

    class Meta:
        abstract = True


class CardPriceData(models.Model):
    c = (
        ('yes', 'Yes', ),
        ('no', 'No', ),
    )

    sku = models.CharField(max_length=255, default='', blank=True)
    name = models.CharField(max_length=255, default='')
    expansion = models.CharField(max_length=255, default='', blank=True)
    product_id = models.CharField(max_length=255, default='', unique=True)
    tcg_direct_price = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True)
    direct_net = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True)
    tcg_price = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True)
    tcg_market = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True)
    tcg_net = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True)
    amazon_price = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True)
    amazon_net = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True)
    scg_buylist = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True)
    ck_buylist = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True)
    cfb_buylist = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True)
    low_store_stock = models.CharField(max_length=3, default='No', choices=c)
    store_quantity_needed = models.IntegerField(default=0)
    printing = models.CharField(max_length=255, default='')
    sell_to = models.CharField(max_length=255, default='')
    best_net = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class DailyMtgNews(models.Model):
    title = models.CharField(max_length=255, default='')
    link = models.URLField(default='')
    description = models.TextField(default='')
    published_date = models.CharField(max_length=255, default='')
    creator = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title


class MooseAutopriceMetrics(models.Model):
    name = models.CharField(max_length=255, default='')
    expansion = models.CharField(max_length=255, default='')
    condition = models.CharField(max_length=255, default='')
    printing = models.CharField(max_length=255, default='')
    language = models.CharField(max_length=255, default='')
    sku = models.CharField(max_length=255, default='')
    updated_price = models.CharField(max_length=255, default='')
    updated_at = models.DateTimeField(auto_now=True)
    old_price = models.CharField(max_length=255, default='')
    price_1 = models.CharField(max_length=255, default='')
    price_1_gold = models.BooleanField(default=False, blank=True)
    price_2 = models.CharField(max_length=255, default='', blank=True)
    price_2_gold = models.BooleanField(default=False, blank=True)
    price_3 = models.CharField(max_length=255, default='', blank=True)
    price_3_gold = models.BooleanField(default=False)
    price_4 = models.CharField(max_length=255, default='', blank=True)
    price_4_gold = models.BooleanField(default=False, blank=True)
    price_5 = models.CharField(max_length=255, default='', blank=True)
    price_5_gold = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.name}({self.expansion})'


class MooseInventory(models.Model):
    name = models.CharField(max_length=255, default='')
    expansion = models.CharField(max_length=255, default='')
    condition = models.CharField(max_length=255, default='')
    printing = models.CharField(max_length=255, default='')
    seller_1_name = models.CharField(max_length=255, default='')
    seller_1_total_sales = models.CharField(max_length=255, default='')
    seller_1_total_price = models.CharField(max_length=255, default='')
    seller_2_name = models.CharField(max_length=255, default='')
    seller_2_total_sales = models.CharField(max_length=255, default='')
    seller_2_total_price = models.CharField(max_length=255, default='')
    updated_price = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name


class MTG(BasicCardInfo):
    image_url = models.CharField(max_length=255, default='')
    language = models.CharField(max_length=255, default='English')
    set_abbreviation = models.CharField(max_length=255, default='', blank=True)
    rarity = models.CharField(max_length=255, default='', blank=True)
    oracle_text = models.TextField(default='', blank=True)
    flavor_text = models.TextField(default='', blank=True)
    colors = models.CharField(max_length=255, default='', blank=True)
    color_identity = models.CharField(max_length=255, default='', blank=True)
    card_type = models.CharField(max_length=255, default='', blank=True)
    subtypes = models.CharField(max_length=255, default='', blank=True)
    loyalty = models.CharField(max_length=255, default='', blank=True)
    power = models.CharField(max_length=255, null=True, default=None, blank=True)
    toughness = models.CharField(max_length=255, null=True, default=None, blank=True)
    layout = models.CharField(max_length=255, default='', blank=True)
    artist = models.CharField(max_length=255, default='', blank=True)
    collector_number = models.CharField(max_length=255, default='', blank=True)
    mana_cost = models.CharField(max_length=255, default='', blank=True)
    mana_cost_encoded = models.CharField(max_length=255, default='', blank=True)
    converted_mana_cost = models.DecimalField(max_digits=10, decimal_places=1, null=True, default=None, blank=True)
    converted = models.BooleanField(default=False)
    foil_only = models.BooleanField(default=False)
    normal_only = models.BooleanField(default=False)
    preorder = models.BooleanField(default=False)
    solid_color = models.CharField(max_length=255, default='', blank=True)
    sick_deal = models.BooleanField(default=False)
    sick_deal_percentage = models.IntegerField(default=0)
    normal_hotlist = models.BooleanField(default=False)
    normal_hotlist_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    foil_hotlist = models.BooleanField(default=False)
    foil_hotlist_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    normal_buylist = models.BooleanField(default=False)
    normal_buylist_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    normal_buylist_max_quantity = models.IntegerField(default=0)
    foil_buylist = models.BooleanField(default=False)
    foil_buylist_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    foil_buylist_max_quantity = models.IntegerField(default=0)
    release_date = models.DateTimeField()
    restock_notice = models.ManyToManyField("customer.CustomerRestockNotice", blank=True)

    def __str__(self):
        return self.name

    @property
    def is_preorder(self):
        return self.release_date > datetime.now(pytz.timezone('EST'))

    @property
    def in_stock(self):
        return True if self.normal_clean_stock > 0 or self.normal_played_stock > 0 or self.normal_heavily_played_stock > 0 \
            or self.foil_clean_stock > 0 or self.foil_played_stock > 0 or self.foil_heavily_played_stock > 0 else False

    class Meta:
        verbose_name_plural = "MTG Card Database"
        ordering = ['name', ]


class MtgCardInfo(models.Model):
    name = models.CharField(max_length=255, default='')
    card_identifier = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name", ]


class MTGDatabase(models.Model):
    name = models.CharField(max_length=255, default='', db_index=True)
    expansion = models.CharField(max_length=255, default='', db_index=True)
    sku = models.CharField(max_length=255, default='', unique=True)
    product_id = models.CharField(max_length=255, default='')
    printing = models.CharField(max_length=255, default='')
    condition = models.CharField(max_length=255, default='')
    language = models.CharField(max_length=255, default='')
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __string__(self):
        return self.name


class MTGUpload(BasicCardInfo):
    upload_status = models.BooleanField(default=False)
    date_time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SickDeal(MTG):
    pass


class StateInfo(models.Model):
    name = models.CharField(max_length=255, default='')
    abbreviation = models.CharField(max_length=2, default='')
    state_tax_rate = models.DecimalField(max_digits=12, decimal_places=5, default=0)
    local_tax_rate = models.DecimalField(max_digits=12, decimal_places=5, default=0)

    def __str__(self):
        return self.name


class TcgCredentials(models.Model):
    name = models.CharField(max_length=20, default='', blank=True)
    token = models.TextField(default='')


class TcgGroupPrice(models.Model):
    product_id = models.CharField(max_length=255, default='')
    printing = models.CharField(max_length=255, default='')
    low_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    mid_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    market_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    direct_low_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_id




