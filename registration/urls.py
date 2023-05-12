
from django.contrib import admin
from django.urls import include, path
from registration.views import home, lead_register
urlpatterns = [
    path('', lead_register, name='registration'),  # change the root path to lead_register
    path('home/', home, name='home'),
    path('registration/', lead_register, name='registration'),
    path('admin/', admin.site.urls),
]