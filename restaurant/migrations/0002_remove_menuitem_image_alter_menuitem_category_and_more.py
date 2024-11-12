# Generated by Django 5.1.2 on 2024-10-25 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='image',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.CharField(choices=[('entradas', 'Entradas'), ('carne', 'Carne'), ('peixe', 'Peixe'), ('sobremesas', 'Sobremesas'), ('bebidas', 'Bebidas')], max_length=20),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
