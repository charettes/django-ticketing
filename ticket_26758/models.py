from __future__ import unicode_literals

from django.db import models

class Company(models.Model):
    owner_id = models.IntegerField(blank=True, null=True)
    company_recid = models.IntegerField(primary_key=True)
    company_id = models.CharField(max_length=50, blank=True)
    company_name = models.CharField(max_length=50, blank=True)

class SrService(models.Model):
    owner_id = models.IntegerField(blank=True, null=True)
    sr_service_recid = models.IntegerField(primary_key=True)
    #sr_location_recid = models.ForeignKey('SrLocation', db_column='sr_location_recid', blank=True, null=True)
    company_recid = models.ForeignKey('Company', db_column='company_recid')
