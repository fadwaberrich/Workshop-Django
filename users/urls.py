from .views import *
from django.urls import path
from django.contrib.auth.views import LogoutView
#appel tt les url dans 
urlpatterns = [
    path('login/', login_view,name="login"),
    path('register/', register,name="register"),
    path('logout/', LogoutView.as_view(),name="logout"),
]
