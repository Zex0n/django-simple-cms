from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext


class Setting(models.Model):

    phone1=models.CharField(_("Телефонный номер 1"), max_length=200, default='', blank=True)
    phone2=models.CharField(_("Телефонный номер 2"), max_length=200, default='', blank=True)
    email1=models.EmailField(_("E-mail 1"), blank=True)
    email2=models.EmailField(_("E-mail 2"), blank=True)
    mainadress=models.CharField(_("Адрес"), max_length=200, default='', blank=True)


    class Meta:
        verbose_name = _("Настройка")
        verbose_name_plural = _("Настройки")




