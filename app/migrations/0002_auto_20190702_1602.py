# Generated by Django 2.2.3 on 2019-07-02 10:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
