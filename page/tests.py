from django.test import TestCase, RequestFactory

import datetime

from django.utils import timezone
from django.contrib.auth.models import AnonymousUser, User

from .models import Carousel
from model_mommy import mommy


class CarouselMethodTests(TestCase):
    def test_form_creation_mommy(self):
        new_Carousel = mommy.make(Carousel, template='0')
        self.assertTrue(isinstance(new_Carousel, Carousel))
        self.assertEqual(new_Carousel.__str__(), new_Carousel.title)
