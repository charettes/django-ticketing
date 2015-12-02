from django.test import TestCase

from . import models

class AmpTests(TestCase):
    def test_querying(self):
        models.Foo.objects.create(bar='Fish & Chips')
        self.assertTrue(models.Foo.objects.filter(bar__icontains='Fish &').exists())
        self.assertTrue(models.Foo.objects.filter(bar__icontains='Fish & Chips').exists())
        self.assertFalse(models.Foo.objects.filter(bar__icontains='Fish &amp; Chips').exists())
