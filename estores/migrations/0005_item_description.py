# Generated by Django 4.0.3 on 2022-03-25 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estores', '0004_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='This is a good product for everyone to buy.'),
            preserve_default=False,
        ),
    ]
