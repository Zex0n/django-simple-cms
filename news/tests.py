from django.test import TestCase, RequestFactory

import datetime

from django.utils import timezone
from django.contrib.auth.models import AnonymousUser, User

from .models import News
from model_mommy import mommy


class DealersMethodTests(TestCase):
    def test_form_creation_mommy(self):
        new_row = mommy.make(News, text='<b>sometext</b>')
        self.assertTrue(isinstance(new_row, News))

