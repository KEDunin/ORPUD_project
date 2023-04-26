from django.shortcuts import render

def main_view(request):
    return render(request, 'web_analytics_service/main.html')
