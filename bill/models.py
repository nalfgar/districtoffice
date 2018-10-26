from django.db import models
from django.utils.timezone import now

from change.models import Change


# def get_sellings():
#     return Change.objects.filter(invoiced=False, document_type__factor=1.30).count()
#
# def get_big_changes():
#     return Change.objects.filter(invoiced=False, document_type__factor=1.00).count()
#
#
# def get_small_changes():
#     return Change.objects.filter(invoiced=False, document_type__factor=0.15).count()



class Bill(models.Model):
    number = models.IntegerField('numer')
    data = models.DateField('data', default=now)

    sellings = models.SmallIntegerField('ilość sprzedaży', default=20)
    big_changes = models.SmallIntegerField('ilość dużych zmian', default=20)
    small_changes = models.SmallIntegerField('ilość małych zmian', default=40)

    def __str__(self):
        return 'sellings:{}'.format(Change.objects.filter(invoiced=False, document_type__factor=1.30).count(),)
