from django.db import models
from django.utils import timezone


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name=u'Заголовок новости')
    text = models.TextField(verbose_name=u'Текст новости')
    created_date = models.DateTimeField(verbose_name=u'Дата создания', editable=False, auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now, blank=False, null=False, verbose_name=u'Дата для вывода')
    start_date = models.DateTimeField(default=timezone.now, blank=False, null=False, verbose_name=u'Дата начала показа')
    end_date = models.DateTimeField(default=timezone.now, blank=True, null=False, verbose_name=u'Дата завершения показа')
    main_page = models.BooleanField(verbose_name=u'На главную', default=False)
    file = models.ImageField(upload_to='news', verbose_name=u'Изображение',null=True, blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

    def get_last_news(cols=3):
        return News.objects.order_by('-published_date')[:cols]
