# Generated by Django 3.2.4 on 2021-07-01 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210701_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sold_product',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]