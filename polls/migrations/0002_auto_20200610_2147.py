# Generated by Django 3.0.3 on 2020-06-10 13:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textz',
            name='text_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 10, 13, 47, 13, 497324, tzinfo=utc)),
        ),
    ]
