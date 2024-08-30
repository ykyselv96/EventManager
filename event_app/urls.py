from django.urls import path
from . import views


urlpatterns = [
    path('events/', views.EventApiView.as_view(), name='list_of_events'),
    path('events/<int:pk>/', views.EventDetailApiView.as_view(), name='event'),
    path('events/register/', views.RegistrationView.as_view(), name='event_register'),
]
