from django.contrib import admin
from django.urls import path

from web_analytics_service.views import main_view, registration_view

urlpatterns = [
    path('', main_view, name='main'),
    path('registration/', registration_view)
]
