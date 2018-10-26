# Generated by Django 2.1.2 on 2018-10-21 10:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Change',
            fields=[
                ('data', models.DateTimeField(auto_created=True, default=django.utils.timezone.now, editable=False, verbose_name='Data')),
                ('year', models.IntegerField(auto_created=True, default=2018, editable=False, verbose_name='Rok')),
                ('number', models.AutoField(primary_key=True, serialize=False, verbose_name='Lp.')),
                ('edicta', models.IntegerField(blank=True, null=True, verbose_name='EDICTA')),
                ('documentSignature', models.CharField(max_length=32, unique=True, verbose_name='sygnatura dokumentu')),
                ('description', models.CharField(default='', editable=False, max_length=64, verbose_name='informacje dodatkowe')),
                ('community', models.CharField(choices=[('2613012', 'Kluczewsko'), ('2613022', 'Krasocin'), ('2613032', 'Moskorzew'), ('2613042', 'Radków'), ('2613052', 'Secemin'), ('2613064', 'miasto Włoszczowa'), ('2613065', 'gmina Włoszczowa')], max_length=16, verbose_name='gmina')),
                ('invoiced', models.BooleanField(default=False, editable=False, verbose_name='Zafakturowana')),
                ('sended', models.BooleanField(default=False, editable=False, verbose_name='Wysłana')),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField(blank=True, null=True, verbose_name='numer obrębu')),
                ('proofOfChange', models.IntegerField(verbose_name='dowód zmiany')),
                ('unitOfRegistration', models.BooleanField(default=False, verbose_name='tylko jednostka')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False, verbose_name='Lp.')),
                ('type', models.CharField(max_length=32, verbose_name='Typ')),
                ('description', models.CharField(max_length=32, verbose_name='rodzaj dokumentu')),
                ('factor', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='współczynnik')),
            ],
        ),
        migrations.AddField(
            model_name='change',
            name='document_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='change.DocumentType'),
        ),
        migrations.AddField(
            model_name='change',
            name='precinct',
            field=models.ForeignKey(on_delete='numer obrębu', to='change.Community'),
        ),
    ]
