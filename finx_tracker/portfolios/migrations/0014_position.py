# Generated by Django 3.2.13 on 2022-08-21 21:31

from django.db import migrations, models
import finx_tracker.portfolios.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0013_auto_20220821_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acct_alias', models.IntegerField()),
                ('portfolio', models.ForeignKey(on_delete=finx_tracker.portfolios.models.on_delete_callable, to='portfolios.portfolio')),
            ],
            options={
                'db_table': 'portfolios_position',
            },
        ),
    ]