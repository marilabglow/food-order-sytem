# Generated by Django 3.2.12 on 2022-11-29 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20221129_0606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='food_name',
            new_name='food',
        ),
    ]
