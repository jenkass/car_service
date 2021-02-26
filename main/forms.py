from django import forms
from .models import AdvUser, Order, Cat
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError


class ChangeIserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Адрес электронной почты')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name')


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Адрес электронной почты')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput, help_text=
    password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль (повторно)', widget=forms.PasswordInput, help_text=
    'Введите тот же самый пароль еще раз для проверки')

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('Введенные пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_activated = True
        if commit:
            user.save()
        return user

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')


class OrderForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Cat.objects.all(), empty_label=None, label='Категория')
    date = forms.DateTimeField(label='Дата/время заказа')
    number = forms.CharField(label='Ваш номер')

    class Meta:
        model = Order
        fields = '__all__'
        widgets = {'author': forms.HiddenInput, 'is_active': forms.HiddenInput}
