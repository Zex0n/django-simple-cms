from page.models import Banners


def banners(request):

    offer=Banners.objects.all()

    return {"banners":offer}
