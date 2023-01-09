from django.shortcuts import render, HttpResponseRedirect
from user.models import User
from user.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from products.models import Basket


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация выполнена успешно')
            return HttpResponseRedirect(reverse('user:login'))
            context = {'form': form, 'user': True}
    else:
        form = UserRegisterForm()
        context = {'form': form, 'user': False}

    return render(request, "user/register.html", context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)

    else:
        form = UserLoginForm()
    context = {'form': form}

    return render(request, "user/login.html", context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user,
                               data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('user:profile'))
        else:
            print(form.errors)

    else:
        form = UserProfileForm(instance=request.user)
    basket = Basket.objects.filter(user=request.user)

    context = {"title": "Store-профиль",
               'form': form,
               'basket': basket


               }
    return render(request, 'user/profile.html', context)
