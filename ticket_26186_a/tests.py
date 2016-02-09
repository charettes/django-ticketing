from django.test import TestCase

from .models import Model2


class RelToTests(TestCase):
    def test_model1(self):
        self.assertEqual(
            Model2._meta.get_field('model1').rel.to._meta.app_label,
            'ticket_26186_a'
        )
