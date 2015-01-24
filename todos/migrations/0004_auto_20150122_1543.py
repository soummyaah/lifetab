# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_remove_todo_archived'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='done',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='notes',
        ),
    ]
