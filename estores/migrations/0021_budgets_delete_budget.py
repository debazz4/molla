# Generated by Django 4.0.3 on 2023-07-06 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estores', '0020_budget'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budgets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_name', models.CharField(max_length=12)),
                ('amount', models.FloatField()),
                ('duration', models.CharField(max_length=3)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Budget',
        ),
    ]