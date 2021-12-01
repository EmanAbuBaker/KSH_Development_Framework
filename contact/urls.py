from django.urls import path

from accounts.views import my_view
from .views import ContactView, ContactSuccessView
from accounts import views

app_name = 'contact'

urlpatterns = [
    path('', ContactView.as_view(), name="contact"),
    path('success/', ContactSuccessView.as_view(), name="success"),
    
    
]