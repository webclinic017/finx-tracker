# Generated by Django 3.2.13 on 2022-08-24 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0015_auto_20220821_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouping',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('closed', 'Active')], default='active', max_length=6),
        ),
    ]
