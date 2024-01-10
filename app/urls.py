from django.urls import path
from app import views

urlpatterns = [
    path('events/', views.eventlist, name='event_list'),
    path('eventd/<int:event_id>/', views.eventdetail, name='event_detail'),
    path('events/register/', views.registerforevent, name='registerforevent'),
]