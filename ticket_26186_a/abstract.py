from __future__ import unicode_literals

from django.db import models


class AbstractModel1(models.Model):
    class Meta:
        abstract = True


class AbstractModel2(models.Model):
    model1 = models.ForeignKey('Model1')

    class Meta:
        abstract = True
