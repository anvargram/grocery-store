from django.urls import path
from . views import(
    profiles,
    user_register,
    user_login,
    user_logout
)


urlpatterns = [
    path('profile/', profiles, name='profile'),
    path('login/', user_login, name='login'),
    path('registration/', user_register, name='registration'),
    path('logout/', user_logout, name='logout')
    ]