from django.contrib import admin

# for email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect

# Register your models here.
from . import models

class AppointmentAdmin(admin.ModelAdmin):
    list_display = [
        "doctor_name",
        "patient_name",
        "appointment_type",
        "appointment_status",
        "symptom",
        "time",
        "cancel",
    ]

    def patient_name(self, obj):
        return obj.patient.user.first_name

    def doctor_name(self, obj):
        return obj.doctor.user.first_name

    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appointment_status == "Running" and obj.appointment_type == "Online":
            email_subject = "Your online Appointment is Running"
            email_body = render_to_string(
                "admin_email.html", {"user": obj.patient.user, "doctor": obj.doctor}
            )
            email = EmailMultiAlternatives(
                email_subject, "", to=[obj.patient.user.email]
            )
            email.attach_alternative(email_body, "text/html")
            email.send()


admin.site.register(models.Appointment, AppointmentAdmin)
