from django.test import TestCase
from .models import Carousel, Page, MenuSection, Menu
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key


class CarouselMethodTests(TestCase):
    def test_form_creation_mommy(self):
        new_Carousel = mommy.make(Carousel, template='0')
        self.assertTrue(isinstance(new_Carousel, Carousel))
        self.assertEqual(new_Carousel.__str__(), new_Carousel.title)


class PageMethodTests(TestCase):
    def test_form_creation_mommy(self):
        new_row = mommy.make(Page, content='<b>sometext</b>')
        self.assertTrue(isinstance(new_row, Page))

