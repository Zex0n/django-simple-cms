# django-simple-cms
Very  simple cms for easy and small sites

###The project is under development. The present version is not working.

### Insert menu in template
You should set menu template and the slug for this menu in admin area. And then you can insert menu in the template like

    {% include menu.MENU_SLUG.get_template %}

For example:

    <div id="navbar" class="navbar-collapse collapse">
        {% include menu.mainmenu.get_template %}
    </div>
 
where "mainmenu" is a slug of the menu.

If you need more, than one menu template, you can configure it in the settings.py:

    MENU_TEMPLATES = (
        # Customize this
        (1, 'vertical_menu.html'),
        (2, 'horizontal_menu.html')
    )