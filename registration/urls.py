
from django.contrib import admin
from django.urls import include, path
from registration.views import home, lead_register
urlpatterns = [
    path('home/',home, name='home'),
    path('registration/',lead_register, name='registration'),
]
