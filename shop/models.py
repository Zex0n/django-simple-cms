from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager
from urllib.parse import urljoin
from django.core.urlresolvers import resolve, reverse
from django.conf import settings
from django.core.cache import cache
from multiselectfield import MultiSelectField
from django.utils.functional import lazy
from ckeditor_uploader.fields import RichTextUploadingField

class BaseShop(models.Model):
    created_date = models.DateTimeField(_("Дата создания"), auto_now_add=True, editable=False)
    edited_date = models.DateTimeField(_("Дата редактирования"), auto_now=True, editable=False, null=True)

    title = models.CharField(_("Название"), max_length=1000, default='')
    meta_description = models.CharField(_("Description"), max_length=1000, blank=True)
    meta_keywords = models.CharField(_("Keywords"), max_length=1000, blank=True)
    slug = models.SlugField(_("Имя для url"), unique=True, blank=True, help_text=_("Только английские буквы, цифры и знаки минус и подчеркивание."))
    tags = TaggableManager(_("Тэги"), blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Category(MPTTModel, BaseShop):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, verbose_name=u"Родительский элемент")
    content = RichTextUploadingField("Описание", blank=True)

    class Meta:
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")


class Item(BaseShop):
    content = RichTextUploadingField("Описание", blank=True)
    category = models.ManyToManyField(Category, verbose_name=u'Категория')
    status = models.BooleanField("Опубликовано", default=True)

    class Meta:
        verbose_name = _("Товар")
        verbose_name_plural = _("Товары")


class Item_variation(models.Model):
    title = models.CharField(_("Название"), default='', max_length=255)
    vendor_code = models.CharField(_("Артикул"), blank=True, max_length=255)
    default_variation = models.BooleanField(_("Вариация по умолчанию"), default=False)
    stock = models.IntegerField(_("На складе"), default=0)
    price_1 = models.DecimalField(_("Цена 1"), max_digits=10, decimal_places=2, blank=True, null=True)
    price_2 = models.DecimalField(_("Цена 2"), max_digits=10, decimal_places=2, blank=True, null=True)
    price_3 = models.DecimalField(_("Цена 3"), max_digits=10, decimal_places=2, blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    num = models.IntegerField(_("Порядковый номер"), default=0, blank=True, db_index=True)

    class Meta:
        verbose_name = _("Вариация")
        verbose_name_plural = _("Вариации")

    def __str__(self):
        return self.title


class Item_image(models.Model):
    title = models.CharField(_("Название"), max_length=1000, default='')
    file = models.ImageField(_("Изображение"), upload_to='shop')
    item_variation = models.ForeignKey(Item_variation, on_delete=models.CASCADE, blank=True)
    num = models.IntegerField(_("Порядковый номер"), default=0, blank=True, db_index=True)

    class Meta:
        verbose_name = _("Изображение")
        verbose_name_plural = _("Изображения")


    def __str__(self):
        return self.title
