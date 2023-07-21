# Generated by Django 4.0.3 on 2023-07-13 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estores', '0023_coupon_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirts'), ('SW', 'Sport wears'), ('OW', 'Outwears'), ('D', 'Dresses'), ('T', 'T-shirts'), ('J', 'Jackets'), ('SH', 'Shoes'), ('JP', 'Jumpers'), ('JN', 'Jeans'), ('C', 'Caps')], max_length=2),
        ),
    ]
