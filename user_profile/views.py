from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from .models import UserProfile
from shop.models import Category, Item, Item_variation, Order, OrderItem, Status, UserProfile
from .forms import UserProfileForm

from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied


@login_required
def edit_user(request):
    user_id = request.user.id
    user = User.objects.get(pk=user_id)
    user_form = UserProfileForm(instance=user)

    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=(
        'name',
        'phone',
        'company_name',
        'inn',
        'kpp',
        'orgn',
        'bank',
        'bik',
        'rs',
        'ks',
        'city',
        'adres',
    ), can_delete=False)

    formset = ProfileInlineFormset(instance=user)


    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserProfileForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/accounts/profile/')

        return render(request, "user_profile/edit_user.html", {
            "noodle": user_id,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied

def orders_history(request):
    user_id = request.user.id
    user = User.objects.get(pk=user_id)
    order_list = Order.objects.filter(customer=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        return render(request, "user_profile/orders_history.html", {
            "order_list": order_list,
        })
    else:
        raise PermissionDenied