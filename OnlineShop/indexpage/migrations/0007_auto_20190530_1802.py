# Generated by Django 2.2.1 on 2019-05-30 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexpage', '0006_auto_20190530_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.TextField(choices=[('Shoes', 'Shoes'), ('Clothes', 'Clothes'), ('Accessoiries', 'Accessoiries')]),
        ),
    ]
