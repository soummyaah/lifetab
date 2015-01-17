# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20150116_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='archived',
        ),
    ]
