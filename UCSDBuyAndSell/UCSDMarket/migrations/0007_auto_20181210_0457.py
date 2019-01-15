# Generated by Django 2.0.8 on 2018-12-10 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UCSDMarket', '0006_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='price',
        ),
        migrations.AddField(
            model_name='listing',
            name='Price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
