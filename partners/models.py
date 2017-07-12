from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _, ugettext
from geoposition.fields import GeopositionField
from ckeditor_uploader.fields import RichTextUploadingField


class Regions (models.Model):
    """
    Регионы
    """
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата создания', editable=False)
    edited_date = models.DateTimeField(auto_now=True, verbose_name=u'Дата редактирования', editable=False, null=True)
    title = models.CharField(max_length=255, verbose_name=u'Название')
    num = models.IntegerField(default=0, verbose_name=u'Порядковый номер')

    class Meta:
        verbose_name = _("Регион")
        verbose_name_plural = _("Регионы")
        ordering = ['num']

    def __str__(self):
        return self.title


class Dealers (models.Model):
    """
    Диллеры
    """
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата создания', editable=False)
    edited_date = models.DateTimeField(auto_now=True, verbose_name=u'Дата редактирования', editable=False, null=True)

    title = models.CharField(max_length=255, verbose_name=_('Название'))
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=_("Телефон должен быть введен в следующем формате: '+799999999'. Разрешено до 15 символов."))
    phone_number = models.CharField(validators=[phone_regex], verbose_name=_("Телефон"), blank=True, max_length=15)  # validators should be a list
    address = models.TextField(_("Адрес"), blank=True)
    url = models.URLField(_("Сайт"), blank=True)
    email = models.EmailField(_("E-mail"), blank=True)
    text = RichTextUploadingField(verbose_name=_('Описание'), blank=True)
    show = models.BooleanField(verbose_name=_('Показывать'), default=True)
    file = models.ImageField(upload_to='partners', verbose_name=_('Логотип'),null=True, blank=True)
    region = models.ForeignKey(Regions, on_delete=models.SET_NULL, verbose_name=u'Регион', null=True, blank=True)
    position = GeopositionField(verbose_name=u'Расположение', blank=True)
    num = models.IntegerField(default=0, verbose_name=u'Порядковый номер')

    class Meta:
        verbose_name = _("Диллер")
        verbose_name_plural = _("Диллеры")
        ordering = ['num']

    def __str__(self):
        return self.title

    def get_news_block(cols=3):
        return Dealers.objects.filter(show=True).order_by('title')[:cols]
