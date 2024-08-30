from event_app.models import Event, EventRegistration
from .serializers import EventSerializer, UserSerializer, EventRegistrationSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class EventApiView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class EventDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all()

class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegistrationView(generics.CreateAPIView):
    serializer_class = EventRegistrationSerializer
    permission_classes = (IsAuthenticated,)
    queryset = EventRegistration.objects.all()
