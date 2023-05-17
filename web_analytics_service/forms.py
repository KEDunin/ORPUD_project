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
    number = forms.ChoiceField(
        choices=(
            ('12', '12'),
            ('13', '13'),
            ('14', '14')
        )
    )
    model = forms.ChoiceField(
        choices=(
            ('None', '-'),
            ('Pro', 'Pro'),
            ('Pro Max', 'Pro Max')
        )
    )
    color = forms.ChoiceField(
        choices=(
            ('black', 'black'),
            ('green', 'green'),
            ('blue', 'blue')
        )
    )
    memory = forms.ChoiceField(
        choices=(
            ('128', '128'),
            ('256', '256'),
            ('512', '512')
        )
    )
