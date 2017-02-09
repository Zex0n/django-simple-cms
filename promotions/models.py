from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Promotions(models.Model):
    title = models.CharField(max_length=200, verbose_name=u'Заголовок акции')
    text = RichTextUploadingField(verbose_name=u'Полное описание')
    created_date = models.DateTimeField(verbose_name=u'Дата создания', editable=False, auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now, blank=False, null=False, verbose_name=u'Дата для вывода')
    start_date = models.DateTimeField(default=timezone.now, blank=False, null=False, verbose_name=u'Дата начала показа')
    end_date = models.DateTimeField(default=timezone.now, blank=True, null=False, verbose_name=u'Дата завершения показа')
    main_page = models.BooleanField(verbose_name=u'На главную', default=True)
    file = models.ImageField(upload_to='promotions', verbose_name=u'Изображение',null=True, blank=True)

    class Meta:
        verbose_name = 'Промо акция'
        verbose_name_plural = 'Промо акции'

    def __str__(self):
        return self.title

    def get_promotions_block(cols=3):
        return Promotions.objects.filter(main_page=True, start_date__lte=timezone.now, end_date__gte=timezone.now).order_by('-published_date')[:cols]
