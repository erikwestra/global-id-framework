# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('session_token', models.TextField()),
                ('last_access', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, unique=True, db_index=True)),
                ('pass_salt', models.TextField()),
                ('pass_hash', models.TextField()),
                ('type', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='user',
            field=models.ForeignKey(to='authentication.User'),
        ),
    ]
