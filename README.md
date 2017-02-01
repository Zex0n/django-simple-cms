# django-simple-cms
Very  simple cms for easy and small sites

The project is under development. The present version is not working.

### Insert menu in template
You should set the slug for menu in admin area. And then you can insert menu in the template like 
`{% include menu.MENU_SLUG.get_template %}`.

For example:

    <div id="navbar" class="navbar-collapse collapse">
        {% include menu.mainmenu.get_template %}
    </div>
 
where mainmenu is a slug of the menu.
