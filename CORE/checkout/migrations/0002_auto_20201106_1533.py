# Generated by Django 3.0.8 on 2020-11-06 14:33

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaddress',
            name='country',
            field=django_countries.fields.CountryField(default='COUNTRY', max_length=250),
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='landmark',
            field=models.CharField(max_length=50),
        ),
    ]
