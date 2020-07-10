# Generated by Django 3.0.3 on 2020-06-10 13:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200610_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unfavourable',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('favourite', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='textz',
            name='text_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 10, 13, 48, 46, 129902, tzinfo=utc)),
        ),
    ]
