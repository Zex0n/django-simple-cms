from django.shortcuts import render, HttpResponseRedirect, HttpResponse, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from .models import UserProfile
from shop.models import Category, Item, Item_variation, Order, OrderItem, Status, UserProfile
from .forms import RegisterForm1,RegisterForm2

from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied


import django


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

@login_required
def orders_history(request):
    user_id = request.user.id
    user = User.objects.get(pk=user_id)

    if request.user.is_authenticated() and request.user.id == user.id:
        order_list = Order.objects.filter(customer=user)

        return render(request, "user_profile/orders_history.html", {
            "order_list": order_list,
        })
    else:
        raise PermissionDenied




def user_register(request):
    uf = RegisterForm1(request.POST)
    upf = RegisterForm2(request.POST)
    if request.method == 'POST':
        if uf.is_valid() * upf.is_valid():

            uf.is_valid = False
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()

            return HttpResponseRedirect("/shop/")
        else:
            return render(request, 'registration/test_new_register.html', dict(userform=uf, userprofileform=upf))

    else:

        return render(request,'registration/test_new_register.html',dict(userform=uf,userprofileform=upf))


        # else:
        #     uf = RegisterForm1(prefix='user')
        #     upf = RegisterForm2(prefix='userprofile')
        # return render(request,'registration/registration_base.html')