from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
from sorl.thumbnail import ImageField


class Category(models.Model):
    created_date = models.DateTimeField(_("Дата создания"), auto_now_add=True, editable=False)
    edited_date = models.DateTimeField(_("Дата редактирования"), auto_now=True, editable=False, null=True)
    title = models.CharField(_("Название"), max_length=1000, default='')
    meta_description = models.CharField(_("Description"), max_length=1000, blank=True)
    meta_keywords = models.CharField(_("Keywords"), max_length=1000, blank=True)
    slug = models.SlugField(_("Имя для url"), unique=True, blank=True, help_text=_("Только английские буквы, цифры и знаки минус и подчеркивание."))
    content = RichTextField("Описание", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Раздел галлереи")
        verbose_name_plural = _("Разделы галлереи")
        ordering = ['title', ]


class Item(models.Model):
    title = models.CharField(_("Название"), max_length=1000, default='')
    # file = ImageSpecField(_("Изображение"), upload_to='gallery', blank=True, sizes=((250,250),))
    file = ImageField(_("Изображение"), upload_to='gallery', blank=True)
    youtube_url = EmbedVideoField(_("Youtube адрес видео"), blank=True)
    num = models.IntegerField(_("Порядковый номер"), default=0, blank=True, db_index=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = _("Изображение")
        verbose_name_plural = _("Изображения")
        ordering = ['num', 'title', ]

    def __str__(self):
        return self.title