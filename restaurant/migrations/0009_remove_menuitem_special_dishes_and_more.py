# Generated by Django 5.1.2 on 2024-11-08 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_menuitem_special_dishes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='special_dishes',
        ),
        migrations.AddField(
            model_name='specialdish',
            name='menu_items',
            field=models.ManyToManyField(blank=True, related_name='special_dishes', to='restaurant.menuitem'),
        ),
    ]
