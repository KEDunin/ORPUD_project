from django.contrib.auth import get_user_model
from django.shortcuts import render
from web_analytics_service.forms import RegistrationForm

User = get_user_model()


def preview_view(request):
    return render(request, 'web_analytics_service/preview.html')


def main_view(request):
    return render(request, 'web_analytics_service/main.html')


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password2'])
            user.save()
            is_success = True
    return render(request, 'web_analytics_service/registration.html',
                  {'form': form, 'is_success': is_success})
