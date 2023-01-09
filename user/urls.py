from django.urls import path
from user.views import login, registration, profile
app_name = 'user'

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', registration, name='registration'),
    path('profile/', profile, name='profile')
]
