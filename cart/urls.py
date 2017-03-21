from django.conf.urls import url, include

urlpatterns = [
    # This pattern must always be the last
    url('', include('easycart.urls'))
]