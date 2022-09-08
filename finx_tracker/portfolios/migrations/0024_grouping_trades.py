# Generated by Django 3.2.13 on 2022-09-03 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0004_alter_trade_trade_id'),
        ('portfolios', '0023_remove_groupingtrade_ext_trade_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouping',
            name='trades',
            field=models.ManyToManyField(through='portfolios.GroupingTrade', to='trades.Trade'),
        ),
    ]