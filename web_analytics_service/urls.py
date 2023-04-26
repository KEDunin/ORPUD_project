from django.contrib import admin
from django.urls import path

from web_analytics_service.views import main_view

urlpatterns = [
    path('', main_view),
]