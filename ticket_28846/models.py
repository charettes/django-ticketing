from django.db import models

from django.db import models

class Foo(models.Model):
    pass

class Bar(models.Model):
   title = models.CharField(max_length=50)
   foos = models.ManyToManyField(Foo)

