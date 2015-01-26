# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='content',
            field=models.TextField(max_length=100000),
            preserve_default=True,
        ),
    ]
