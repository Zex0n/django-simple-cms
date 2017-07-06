from Shop.models import UserSettings
from forms import *

def user_created(sender, user, request, **kwargs):
    form = UserRegForm(request.POST)
    data = user_profile(user=user)
    data.institution = form.data["phone"]
    data.save()

from registration.signals import user_registered
user_registered.connect(user_created)