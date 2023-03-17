from django.urls import path
from user.views import UserLoginView, UserProfileView, UserRegistrationView
from django.contrib.auth import views as authViews
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView


app_name = 'user'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('register/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>', login_required(UserProfileView.as_view()), name='profile'),           #pk-primary key(айди пользователя)
    path('exit/',LogoutView.as_view(), name='exit'),

]
