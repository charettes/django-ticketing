# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160107050803 on 2016-01-07 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar', models.DurationField()),
            ],
        ),
    ]