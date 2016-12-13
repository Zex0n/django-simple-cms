from django import forms
from .models import Menu
from django.contrib import admin
from django.conf import settings



class MenuAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MenuAdminForm, self).__init__(*args, **kwargs)
        self.fields['template'].choices = self.fields['template'].choices + get_menu_templates()

def get_menu_templates():
    templates = list(getattr(settings, 'MENU_TEMPLATES', []))
    return templates

# def get_templates():
#     from cms.utils.django_load import load_from_file
#     if getattr(settings, 'CMS_TEMPLATES_DIR', False):
#         tpldir = getattr(settings, 'CMS_TEMPLATES_DIR', False)
#         # CMS_TEMPLATES_DIR can either be a string poiting to the templates directory
#         # or a dictionary holding 'site: template dir' entries
#         if isinstance(tpldir, dict):
#             tpldir = tpldir[settings.SITE_ID]
#         # We must extract the relative path of CMS_TEMPLATES_DIR to the neares
#         # valid templates directory. Here we mimick what the filesystem and
#         # app_directories template loaders do
#         prefix = ''
#         # Relative to TEMPLATE['DIRS'] for filesystem loader
#
#         path = [template['DIRS'][0] for template in settings.TEMPLATES]
#
#         for basedir in path:
#             if tpldir.find(basedir) == 0:
#                 prefix = tpldir.replace(basedir + os.sep, '')
#                 break
#         # Relative to 'templates' directory that app_directory scans
#         if not prefix:
#             components = tpldir.split(os.sep)
#             try:
#                 prefix = os.path.join(*components[components.index('templates') + 1:])
#             except ValueError:
#                 # If templates is not found we use the directory name as prefix
#                 # and hope for the best
#                 prefix = os.path.basename(tpldir)
#         config_path = os.path.join(tpldir, '__init__.py')
#         # Try to load templates list and names from the template module
#         # If module file is not present skip configuration and just dump the filenames as templates
#         if os.path.isfile(config_path):
#             template_module = load_from_file(config_path)
#             templates = [(os.path.join(prefix, data[0].strip()), data[1]) for data in template_module.TEMPLATES.items()]
#         else:
#             templates = list((os.path.join(prefix, tpl), tpl) for tpl in os.listdir(tpldir))
#     else:
#         templates = list(getattr(settings, 'CMS_TEMPLATES', []))
#     if get_cms_setting('TEMPLATE_INHERITANCE'):
#         templates.append((constants.TEMPLATE_INHERITANCE_MAGIC, _('Inherit the template of the nearest ancestor')))
#     return templates
