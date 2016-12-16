from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager
from urllib.parse import urljoin
from django.core.urlresolvers import resolve, reverse
from multiselectfield import MultiSelectField
from django.utils.functional import lazy
from smallcms.templatetags.cms_tags import get_all_placeholders


class BasePage(MPTTModel):
    """
    Exists solely to store ``PageManager`` as the main manager.
    If it's defined on ``Page``, a concrete model, then each
    ``Page`` subclass loses the custom manager.
    """
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата создания', editable=False)
    edited_date = models.DateTimeField(auto_now=True, verbose_name=u'Дата редактирования', editable=False, null=True)
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True


class Page(BasePage):
    """
    A page in the page tree. This is the base class that custom content types
    need to subclass.
    """

    PAGE_TYPE_CHOICES = (
        (0, _("Страница")),
        (1, _("Ссылка")),
        (2, _("Приложение")),
    )
    APPLICATION_CHOICES = (
        (0, _("Нет")),
    )

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,
                            verbose_name=u"Родительский элемент")

    in_menus = models.BooleanField(_("Показывать в меню"), blank=True, default=True)
    title = models.CharField(_("Заголовок"), max_length=1000, default='')
    meta_description = models.CharField(_("Description"), max_length=1000, blank=True)
    meta_keywords = models.CharField(_("Keywords"), max_length=1000, blank=True)
    menu_title = models.CharField(_("Название в меню"), max_length=255, null=True, blank=True, help_text=_("Оставьте пустым для использования названия страницы"))
    slug = models.SlugField(_("Имя для url"), unique=True, blank=True, help_text=_("Только английские буквы, цифры и знаки минус и подчеркивание."))
    login_required = models.BooleanField(_("Требуется логин"), default=False,
        help_text=_("Если выбрано, то только залогиненный пользователь может просматривать страницу"))
    content = models.TextField("Текст", blank=True)
    page_type = models.IntegerField(_("Тип страницы"), choices=PAGE_TYPE_CHOICES, default=0)
    redirect_url = models.CharField(_("URL для редиректа"), max_length=1000, default='', blank=True)
    application = models.CharField(_("Приложение"), max_length=255, choices=APPLICATION_CHOICES, default='', blank=True)

    class Meta:
        verbose_name = _("Страница")
        verbose_name_plural = _("Страницы")
        # order_with_respect_to = "parent"


    # It is required to rebuild tree after save, when using order for mptt-tree
    def save(self, *args, **kwargs):
        super(Page, self).save(*args, **kwargs)
        Page.objects.rebuild()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        URL for a page - for ``Link`` page types, simply return its
        slug since these don't have an actual URL pattern. Also handle
        the special case of the homepage being a page object.
        """
        slug = self.slug
        if self.content_model == "link":
            # Ensure the URL is absolute.
            slug = urljoin('/', slug)
            return slug
        if slug == "/":
            return reverse("home")
        else:
            return reverse("page", kwargs={"slug": slug})

    # def save(self, *args, **kwargs):
    #     """
    #     Create the title field using the title up the parent chain
    #     and set the initial value for ordering.
    #     """
    #     # self.set_content_model()
    #
    #     titles = [self.title]
    #     parent = self.parent
    #     while parent is not None:
    #         titles.insert(0, parent.title)
    #         parent = parent.parent
    #     self.title = " / ".join(titles)
    #     super(Page, self).save(*args, **kwargs)


    def description_from_content(self):
        """
        Override ``Displayable.description_from_content`` to load the
        content type subclass for when ``save`` is called directly on a
        ``Page`` instance, so that all fields defined on the subclass
        are available for generating the description.
        """
        if self.__class__ == Page:
            if self.content_model:
                return self.get_content_model().description_from_content()
        return super(Page, self).description_from_content()


class Menu (models.Model):
    MENU_TEMPLATES_CHOICES = (
        (0, 'menu.html'),
    )
    PLACEHOLDERS_CHOICES = (
    )

    title = models.CharField(_("Название меню"), max_length=255, default='')
    template = models.IntegerField(choices=MENU_TEMPLATES_CHOICES, default=0)
    placeholder = MultiSelectField(_("Место для установки в шаблоне"), max_length=255, blank=True, choices=PLACEHOLDERS_CHOICES, help_text=_("Используйте в шаблоне тег {% placeholder horizontal_menu %}"))

    class Meta:
        verbose_name = _("Меню")
        verbose_name_plural = _("Меню")

    def __str__(self):
        return self.title

    def __init__(self, *args, **kwargs):
        super(Menu, self).__init__(*args, **kwargs)
        self._meta.get_field('placeholder').choices = get_all_placeholders()



class MenuSection (MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,
                            verbose_name=u"Родительский элемент")
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True)
    page = TreeForeignKey(Page, on_delete=models.CASCADE, verbose_name=u"Страница")
    title = models.CharField(_("Название в меню"), max_length=255, blank=True, default='', help_text=_("Оставьте пустым для использования названия страницы"))
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name = _("Раздел")
        verbose_name_plural = _("Разделы")
        ordering = ["my_order"]

    class MPTTMeta:
        order_insertion_by = ['my_order']

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.page.__str__()