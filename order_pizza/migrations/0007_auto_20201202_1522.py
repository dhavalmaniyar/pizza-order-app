# Generated by Django 3.1.4 on 2020-12-02 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_pizza', '0006_auto_20201201_1950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizzaorder',
            old_name='created_on',
            new_name='createdOn',
        ),
        migrations.RenameField(
            model_name='pizzaorder',
            old_name='deleted_on',
            new_name='deletedOn',
        ),
        migrations.RenameField(
            model_name='pizzaorder',
            old_name='order_id',
            new_name='orderid',
        ),
        migrations.RenameField(
            model_name='size',
            old_name='created_on',
            new_name='createdOn',
        ),
        migrations.RenameField(
            model_name='size',
            old_name='deleted_on',
            new_name='deletedOn',
        ),
        migrations.RenameField(
            model_name='topping',
            old_name='created_on',
            new_name='createdOn',
        ),
        migrations.RenameField(
            model_name='topping',
            old_name='deleted_on',
            new_name='deletedOn',
        ),
        migrations.RenameField(
            model_name='topping',
            old_name='top_type',
            new_name='topType',
        ),
    ]
