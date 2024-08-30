from rest_framework import serializers
from .models import Event, EventRegistration
from django.contrib.auth.models import User


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate(self, data):

        instance = self.instance

        if self.instance:
            existing_events = Event.objects.exclude(pk=instance.pk)
        else:
            existing_events = Event.objects.all()

        if existing_events.filter(title=data.get('title'), date=data.get('date'),
                                location=data.get('location')).exists():
            raise serializers.ValidationError("Such event already exists")
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
        ref_name = "EventAppUser"

class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = '__all__'

    def validate(self, data):
        user = data.get('user')
        event = data.get('event')
        if EventRegistration.objects.filter(user=user, event=event).exists():
            raise serializers.ValidationError("User already registered for this event.")
        return data
