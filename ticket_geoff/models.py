from __future__ import unicode_literals

from django.db import models


class CustomManager(models.Manager):
    use_in_migrations = True


class AddedCustomManager(models.Manager):
    use_in_migrations = True

class Foo(models.Model):
    objects = AddedCustomManager()

