from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import ugettext_lazy as _, ugettext


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name=u'Заголовок новости')
    small_text = models.CharField(_("Текст новости на главную"), max_length=200, default='', blank=True)
    text = RichTextUploadingField(verbose_name=u'Текст новости')
    published_date = models.DateTimeField(default=timezone.now, blank=False, null=False, verbose_name=u'Дата для вывода')
    file = models.ImageField(upload_to='news', verbose_name=u'Изображение',null=True, blank=True)
    file_news = models.ImageField(upload_to='file_news', verbose_name=u'Изображение для карусели новостей', null=True, blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def get_news_block(cols=3):
        return News.objects.filter(main_page=True).order_by('-published_date')[:cols]
