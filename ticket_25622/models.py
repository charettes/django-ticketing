from __future__ import unicode_literals

import uuid
from django.db import models

from django.contrib.contenttypes.fields import (
    GenericForeignKey, GenericRelation,
)
from django.contrib.contenttypes.models import ContentType

class ModelA(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True)

class ModelB(models.Model):
    model_a_fk = models.ForeignKey('ModelA', to_field='uuid')
    model_c_fk = models.ForeignKey('ModelC')

class ModelC(models.Model):
    pass

