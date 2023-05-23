from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from events.models import Event
from .serializers import EventSerializer

from rest_framework import generics

@api_view(['GET'])
def getEvents(request):
    events=Event.objects.all()
    serializer=EventSerializer(events,many=True)
    return Response(serializer.data)

class EventList(generics.ListAPIView):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    