# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('is_protected', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=2000)),
                ('content', models.CharField(max_length=100000)),
                ('feeling', models.CharField(default=b'HAPP', max_length=4, choices=[(b'HAPP', b'happy'), (b'SADD', b'sad'), (b'NOST', b'nostalgic'), (b'CURI', b'curious'), (b'WOND', b'wonderful')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
