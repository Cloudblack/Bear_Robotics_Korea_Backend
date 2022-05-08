# Generated by Django 4.0.4 on 2022-05-04 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_restaurant_name_restaurant_store_and_more'),
        ('results', '0004_resultmenu_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='restuarants',
            new_name='menus',
        ),
        migrations.AddField(
            model_name='result',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant'),
            preserve_default=False,
        ),
    ]
