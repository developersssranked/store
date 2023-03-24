
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import TemplateView
from user.models import User, EmailVerification
from user.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse,reverse_lazy
from products.models import Basket
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import views as authViews
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from common.views import CommonContextMixin

class UserRegistrationView(CommonContextMixin,SuccessMessageMixin ,CreateView):                #!!!! Миксины в классах должны стоять перед самими вьюхами
    model=User
    form_class=UserRegisterForm
    template_name='user/register.html'
    success_url=reverse_lazy('user:login')
    success_message='Вы успешно зарегестрированы'
    title='Store-регистрация'
class UserLoginView(CommonContextMixin, LoginView):
    template_name="user/login.html"
    form_class=UserLoginForm
    title='Store-авторизация'
   




class UserProfileView(CommonContextMixin,UpdateView):
    model=User
    form_class=UserProfileForm
    template_name='user/profile.html'
    title='Store-Личный кабинет'
    def get_success_url(self):                                               #функция для редиректа, в аргументах нам нужно передавать юзер айди
        return reverse_lazy('user:profile',args=(self.object.id,))                    


    # def get_context_data(self, **kwargs):
    #     context=super(UserProfileView,self).get_context_data()
        
    #     context['basket']= Basket.objects.filter(user=self.object)                     #self.object т.к. мы передаем в model модель user, то мы можем сразу ссылаться на нее через self.object
    #     return context
                                #сделали basket глобальной переменной, так как сделали контекстный процессор, смотри context_processors.py


class EmailVerificationView(CommonContextMixin, TemplateView):
    title='Store-Подтверждение электронной почты'
    template_name='user/email_verification.html'
    def get(self, request, *args, **kwargs):
        code=kwargs.get('code')
        user=User.objects.get(email=kwargs['email'])
        email_verifications=EmailVerification.objects.filter(user=user,code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email=True
            user.save()
            return super(EmailVerificationView,self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))
        