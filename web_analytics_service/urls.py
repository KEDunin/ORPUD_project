from django.contrib import admin
from django.urls import path

from web_analytics_service.views import main_view, preview_view

urlpatterns = [
    path('', preview_view),
    path('main/', main_view, name='main')
]