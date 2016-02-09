from django.db import models

class AbstractModel1(models.Model):
    class Meta:
        abstract = True


class AbstractModel2(models.Model):
    model1 = models.ForeignKey('Model1')

    class Meta:
          abstract = True


class Model1(AbstractModel1):
    pass

class Model2(AbstractModel2):
    pass
