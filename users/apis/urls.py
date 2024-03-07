from django.urls import path
from .views import login, register, profile

urlpatterns = [
    path('login/',login.LoginView),
    path('register/',register.RegisterView),
    path('profile/',profile.ProfileView),
]