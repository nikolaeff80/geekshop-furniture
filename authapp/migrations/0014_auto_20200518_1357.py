# Generated by Django 2.2 on 2020-05-18 10:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0013_auto_20200517_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 20, 10, 57, 18, 503501, tzinfo=utc)),
        ),
    ]
