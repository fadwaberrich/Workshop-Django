from rest_framework import serializers
from events.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model= Event
        #fields="__all__"
        fields=[
            "Title",
            "CATEGORY_CHOICES",
            "State",
        ]