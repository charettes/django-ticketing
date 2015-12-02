# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20151201231107 on 2015-12-02 19:03
from __future__ import unicode_literals

from django.db import migrations

def assert_manager_type(apps, schema_editor):
    from ..models import CustomManager
    Foo = apps.get_model('ticket_geoff', 'Foo')
    assert isinstance(Foo.objects, CustomManager)


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_geoff', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(assert_manager_type, assert_manager_type)
    ]
