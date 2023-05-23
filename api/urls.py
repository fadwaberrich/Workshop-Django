from .views import *
from django.urls import path
#appel tt les url dans 
urlpatterns = [
    path('', getEvents,name="apiGetEvents"),
]
