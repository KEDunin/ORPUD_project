from django.contrib.auth import get_user_model
from django.shortcuts import render
from web_analytics_service.forms import RegistrationForm, FilterForm
from web_analytics_service.models import Iphone

User = get_user_model()


def preview_view(request):
    return render(request, 'web_analytics_service/preview.html')


def main_view(request):
    value = Iphone.objects.all()

    filter = FilterForm(request.GET)
    filter.is_valid()
    filters = filter.cleaned_data
    print(filters)

    if filters['number']:
        value = value.filter(number=filters['number'])

    if filters['model']:
        value = value.filter(model=filters['model'])

    if filters['color']:
        value = value.filter(color=filters['color'])

    if filters['memory']:
        value = value.filter(memory=filters['memory'])

    return render(request, 'web_analytics_service/main.html', {
        "range": value,
        "filter": filter
    })



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
