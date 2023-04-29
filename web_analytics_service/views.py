from django.shortcuts import render

def preview_view(request):
    return render(request, 'web_analytics_service/preview.html')

def main_view(request):
    return render(request, 'web_analytics_service/main.html')


