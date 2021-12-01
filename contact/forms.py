# contact/forms.py
from django import forms
from django.conf import settings
from django.core.mail import send_mail



class ContactForm(forms.Form):
    def send(self):
        send_mail(
            subject="Hello Subject",
            message="Message for mail",
            from_email="s.afifi@sd.zain.com",
            recipient_list=['s.afifi@sd.zain.com']
        )