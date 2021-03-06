# Generated by Django 4.0.4 on 2022-04-13 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=50)),
                ('style', models.CharField(max_length=50)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity_on_hand', models.IntegerField()),
                ('commission_percentage', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
