# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReservedName',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.TextField(unique=True)),
                ('twitter_sources', models.TextField(null=True)),
                ('domain_sources', models.TextField(null=True)),
            ],
        ),
    ]
