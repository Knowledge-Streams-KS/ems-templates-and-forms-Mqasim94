# Event Management System 
# Simplified Requirements:
# 1. Models:

# Event Model:
# title (CharField): The event's name.
# description (TextField): A detailed description of the event.
# date (DateTimeField): The date and time of the event.
# location (CharField): The venue of the event.
# Registration Model:
# event (ForeignKey to Event): The event to which the registration relates.
# name (CharField): The name of the attendee.
# email (EmailField): The email address of the attendee.

from django.db import models
from django.forms import ModelForm

class Event(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=64)

class Registration(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    email = models.EmailField()

