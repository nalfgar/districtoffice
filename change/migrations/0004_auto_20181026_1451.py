# Generated by Django 2.1.2 on 2018-10-26 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('change', '0003_auto_20181026_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='change',
            old_name='send',
            new_name='sended',
        ),
    ]
