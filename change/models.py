from django.db import models
from django.utils.timezone import now

VOIVODESHIP = '26'
COUNTY = '13'

COMMUNITY = (
    ('{}{}0{}'.format(VOIVODESHIP, COUNTY, '12'), 'Kluczewsko'),
    ('{}{}0{}'.format(VOIVODESHIP, COUNTY, '22'), 'Krasocin'),
    ('{}{}0{}'.format(VOIVODESHIP, COUNTY, '32'), 'Moskorzew'),
    ('{}{}0{}'.format(VOIVODESHIP, COUNTY, '42'), 'Radków'),
    ('{}{}0{}'.format(VOIVODESHIP, COUNTY, '52'), 'Secemin'),
    ('{}{}0{}'.format(VOIVODESHIP, COUNTY, '64'), 'miasto Włoszczowa'),
    ('{}{}0{}'.format(VOIVODESHIP, COUNTY, '65'), 'gmina Włoszczowa'),
)


class DocumentType(models.Model):
    number = models.AutoField('Lp.', primary_key=True)
    type = models.CharField('Typ', max_length=32)
    description = models.CharField('rodzaj dokumentu', max_length=32)
    factor = models.DecimalField('współczynnik', max_digits=3, decimal_places=2)

    def __str__(self):
        return '{}\t{}\t{}\t{}'.format(self.number, self.type, self.description, self.factor)


class Community(models.Model):
    number = models.SmallIntegerField('numer obrębu', null=True, blank=True)
    proofOfChange = models.IntegerField('dowód zmiany')
    unitOfRegistration = models.BooleanField('tylko jednostka', default=False)

    def __str__(self):
        return '{}\t{}\t{}'.format(self.number, self.proofOfChange, self.unitOfRegistration)


class Change(models.Model):
    number = models.AutoField('Lp.', primary_key=True)
    year = models.IntegerField('Rok', default=2018, auto_created=True, editable=False)
    data = models.DateTimeField('Data', auto_created=True, default=now, editable=True)

    edicta = models.IntegerField('EDICTA', null=True, blank=True)
    documentSignature = models.CharField('sygnatura dokumentu', max_length=32, unique=True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    description = models.CharField('informacje dodatkowe', max_length=64, default='', editable=False)

    community = models.CharField('gmina', max_length=16, choices=COMMUNITY)
    precinct = models.ForeignKey(Community, 'numer obrębu')

    invoiced = models.BooleanField('Zafakturowana', default=False, editable=False)
    sended = models.BooleanField('Wysłana', default=False, editable=False)

    def __str__(self):
        return '{}'.format(self.documentSignature)
