
from django.contrib import admin
from django.urls import include, path
from registration.views import download_table, home, lead_list, lead_register, leads_data_view,save_to_google_sheet
urlpatterns = [
    path('', lead_register, name='registration'),  # change the root path to lead_register
    path('home/', home, name='home'),
    path('registration/', lead_register, name='registration'),
    path('admin/', admin.site.urls),
    path('leads_view/', lead_list, name='leads_view'),
    path('leads_data/', leads_data_view, name='leads_data'),
    path('download_table/', download_table, name='download_table'),
    path('save-to-google-sheet/', save_to_google_sheet, name='save_to_google_sheet'),
]