from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers

class AppointmentVeiwset(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer