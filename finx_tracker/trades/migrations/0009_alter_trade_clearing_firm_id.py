# Generated by Django 3.2.13 on 2023-06-08 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0008_auto_20230608_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='clearing_firm_id',
            field=models.TextField(blank=True, null=True),
        ),
    ]