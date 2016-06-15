from django.test import TestCase

from django.db.models import Count

from .models import Company

class FooTests(TestCase):
    def test_foo(self):
        qs = Company.objects.annotate(ticketcount=Count('srservice')).exclude(ticketcount=0).order_by('-ticketcount')
        print(list(qs))
