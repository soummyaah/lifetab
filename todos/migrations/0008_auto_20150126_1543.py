# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0007_auto_20150126_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due',
            field=models.DateField(default=datetime.datetime.today, blank=True),
            preserve_default=True,
        ),
    ]
