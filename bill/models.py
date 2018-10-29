from django.db import models
from django.utils.timezone import now

from districtoffice.settings import CHANGE_PRICE, SELLINGS_FACTOR, BIG_FACTOR, SMALL_FACTOR
from districtoffice.settings import FACTOR_FOR_DAREK
from change.models import Change


def get_sellings():
    return Change.objects.filter(invoiced=False, document_type__factor=1.30).count()


def get_big_changes():
    return Change.objects.filter(invoiced=False, document_type__factor=1.00).count()


def get_small_changes():
    return Change.objects.filter(invoiced=False, document_type__factor=0.15).count()


def get_all_month():
    return Change.objects.filter(invoiced=False).count()


def get_podgik_price():
    return (get_sellings() * CHANGE_PRICE * SELLINGS_FACTOR) \
           + ((get_sellings() + get_big_changes()) * CHANGE_PRICE * BIG_FACTOR) \
           + (get_small_changes() * CHANGE_PRICE * SMALL_FACTOR)


def get_darek_price(price):
    gross =  price * FACTOR_FOR_DAREK
    cost_of_earning = gross * 0.20
    for_taxation = gross - cost_of_earning
    tax = for_taxation * 0.18
    net = gross - tax
    return '{:10.2f}, {:10.2f}, {:10.2f}, {:10.2f}, {:10.2f}'.format(gross, cost_of_earning, for_taxation, tax, net)


class Bill(models.Model):
    number = models.IntegerField('numer')
    data = models.DateField('data', default=now)

    sellings = models.SmallIntegerField('ilość sprzedaży', default=20)
    big_changes = models.SmallIntegerField('ilość dużych zmian', default=20)
    small_changes = models.SmallIntegerField('ilość małych zmian', default=40)

    def __str__(self):
        sellings = get_sellings()
        big_changes = sellings + get_big_changes()
        small_changes = get_small_changes()
        podgik_price = get_podgik_price()
        darek_price = get_darek_price(podgik_price)

        return 'all={},\tsellings={},\tbig_changes={},\tsmall_changes={},\tprice={}\tdprice={}'.format(get_all_month(),
                                                                                                       sellings,
                                                                                                       big_changes,
                                                                                                       small_changes,
                                                                                                       podgik_price,
                                                                                                       darek_price)
