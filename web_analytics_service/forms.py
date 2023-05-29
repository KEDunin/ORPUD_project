from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            self.add_error('password1', 'Пароли не совпадают')

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


class FilterForm(forms.Form):
    shop = forms.ChoiceField(
        choices=(
            ('1', 'DNS'),
            ('2', 'Ozon'),
            ('3', 'Yandex Market')
        )
    )
    model = forms.ChoiceField(
        choices=(
            ('10', '10 (X)'),
            ('Xr', 'Xr'),
            ('11', '11'),
            ('11 Pro', '11 Pro'),
            ('12', '12'),
            ('12 Pro', '12 Pro'),
            ('12 Pro Max', '12 Pro Max'),
            ('12 mini', '12 mini'),
            ('13', '13'),
            ('13 Pro', '13 Pro'),
            ('13 Pro Max', '13 Pro Max'),
            ('13 mini', '13 mini'),
            ('14', '14'),
            ('14 Plus', '14 Plus'),
            ('14 Pro', '14 Pro'),
            ('14 Pro Max', '14 Pro Max'),

        )
    )
    color = forms.ChoiceField(
        choices=(
            ('альпийский зеленый', 'альпийский зеленый'),
            ('белый', 'белый'),
            ('глубокий фиолетовый', 'глубокий фиолетовый'),
            ('голубой', 'голубой'),
            ('графитовый', 'графитовый'),
            ('желтый', 'желтый'),
            ('зеленый', 'зеленый'),
            ('золотой', 'золотой'),
            ('космический черный', 'космический черный'),
            ('красный', 'красный'),
            ('небесно-голубой', 'небесно-голубой'),
            ('розовый', 'розовый'),
            ('серебристый', 'серебристый'),
            ('серый', 'серый'),
            ('синий', 'синий'),
            ('сияющая звезда', 'сияющая звезда'),
            ('темная ночь', 'темная ночь'),
            ('тихоокеанский синий', 'тихоокеанский синий'),
            ('фиолетовый', 'фиолетовый'),
            ('черный', 'черный')
        )
    )
    memory = forms.ChoiceField(
        choices=(
            ('64', '64'),
            ('128', '128'),
            ('256', '256'),
            ('512', '512'),
            ('1024', '1024')
        )
    )
