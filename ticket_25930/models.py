from __future__ import unicode_literals

from django.db import models


class Foo(models.Model):
    a = models.TextField(default='')
    b = models.TextField(default='')
