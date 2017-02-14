from django.test import TestCase, RequestFactory

import datetime

from django.utils import timezone
from django.contrib.auth.models import AnonymousUser, User

from .models import Regions, Dealers
from model_mommy import mommy


class RegionsMethodTests(TestCase):
    def test_form_creation_mommy(self):
        new_row = mommy.make(Regions)
        self.assertTrue(isinstance(new_row, Regions))

class DealersMethodTests(TestCase):
    def test_form_creation_mommy(self):
        new_row = mommy.make(Dealers, text='<b>sometext</b>')
        self.assertTrue(isinstance(new_row, Dealers))

