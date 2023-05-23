from .views import *
from django.urls import path
urlpatterns = [ #appel tt les url dans 
    path('', homePage,name="Home_Page"),
    path('homePage/', homePage1,name="Home_Page1"),
    path('listStatic/',listEventsStatic,name="list_Events_Static"),
    path('listEvent/',listEvents,name="list_Events"),
    path('add/',addEvent,name="Add_Events"),
    path('addM/',addEventModel,name="Add_Events_Model"),
    path('listV/',listEventsViews.as_view(),name="Event_ListEvent_V"),
    path('listC/',EventCreateView.as_view(),name="Event_ListEvent_C"),
    path('detail/<int:id>',detailEvent,name="Event_detail"),
    path('detailV/<int:pk>',EventDtails.as_view(),name="Event_detailV"),
    path('update/<int:id>', updateEvent, name='Event_UpdateEvent'),
    path('delete/<int:pk>', EventDeleteView.as_view(), name='Event_DeleteEvent_V'),
    path('participate/<int:id>/', participate, name='Event_Participate'),


]
