from django.contrib.auth import get_user_model
from django.shortcuts import render
from web_analytics_service.forms import RegistrationForm, FilterForm
from web_analytics_service.models import Iphone

User = get_user_model()


def main_view(request):
    value = Iphone.objects.all()  # контейнер, в котором содержатся все объекты, содержащиеся в таблице web_analytics_service_iphone
    value_2 = None  # контейнер, в котором содержатся объекты из основного контейнера, но соответствующие условиям, переданным в форму ввода,
    shop = None

    filter = FilterForm(request.GET)
    filter.is_valid()
    filters = filter.cleaned_data

    # вывод названия магазина, в зависимости от полученного входного параметра shop, введенного пользователем
    if filters:
        if filters['shop'] == '1':
            shop = "DNS"

        elif filters['shop'] == '2':
            shop = "Ozon"

        elif filters['shop'] == '3':
            shop = "Yandex market"

    # фильтрация объектов
    if filters:
        value = value.filter(shop_id=filters['shop'])

    if filters:
        value = value.filter(model=filters['model'])

    if filters:
        value = value.filter(color=filters['color'])

    if filters:
        value = value.filter(memory=filters['memory'])

    # фильтрация по дате сбора данных с сайтов интернет-магазинов
    day1 = value.filter(date_id=1)
    day2 = value.filter(date_id=2)
    day3 = value.filter(date_id=3)
    day4 = value.filter(date_id=4)
    day5 = value.filter(date_id=5)
    day6 = value.filter(date_id=6)
    day7 = value.filter(date_id=7)

    value = value.filter(date_id='7')

    # передача полученных значений в доп. контейнер для отображения содержащихся в нем объектов в форму вывода, в случае если пользователь ввел некоторые данные в форму ввода
    if filters:
        value_2 = value

    return render(request, 'web_analytics_service/main.html', {
        "shop": shop,
        "range": value,
        "list_of_filtered_obj": value_2,
        "filter": filter,
        "day1": day1,
        "day2": day2,
        "day3": day3,
        "day4": day4,
        "day5": day5,
        "day6": day6,
        "day7": day7
    })


def registration_view(request):
    form = RegistrationForm()
    is_success = False  # флаг для отображения на странице сообщения в случае, если он равен True (если данные валидны)
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
