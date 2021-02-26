from django.test import TestCase
from main.forms import *
from django import forms
from django.contrib.auth import password_validation


class TestChangeUserInfoForm(TestCase):

    def setUp(self):
        self.form = ChangeIserInfoForm()

    def test_email_form_filed_label(self):
        self.assertTrue(self.form.fields['email'].label == 'Адрес электронной почты')

    def test_email_form_filed_required(self):
        self.assertTrue(self.form.fields['email'].required == True)


class TestOrderForm(TestCase):

    def setUp(self) -> None:
        self.form = OrderForm()

    def test_category_form_field_label(self):
        self.assertTrue(self.form.fields['category'].label == 'Категория')

    def test_category_form_field_empty_label(self):
        self.assertTrue(self.form.fields['category'].empty_label == None)

    def test_category_form_field_empty_label(self):
        self.assertFalse(self.form.fields['category'].queryset == Cat.objects.all())

    def test_date_form_field_label(self):
        self.assertTrue(self.form.fields['date'].label == 'Дата/время заказа')

    def test_number_form_field_label(self):
        self.assertTrue(self.form.fields['number'].label == 'Ваш номер')


class TestRegisterUserForm(TestCase):

    def setUp(self) -> None:
        self.form = RegisterUserForm()

    def test_email_form_field_label_True(self):
        self.assertTrue(self.form.fields['email'].label == 'Адрес электронной почты')

    def test_email_form_field_required_True(self):
        self.assertTrue(self.form.fields['email'].required == True)

    def test_password1_form_field_label_True(self):
        self.assertTrue(self.form.fields['password1'].label == 'Пароль')

    def test_password1_form_field_widgets_False(self):
        self.assertFalse(self.form.fields['password1'].widget == forms.PasswordInput)

    def test_password1_form_field_help_text_True(self):
        self.assertTrue(
            self.form.fields['password1'].help_text == password_validation.password_validators_help_text_html())

    def test_password2_form_field_label_True(self):
        self.assertTrue(self.form.fields['password2'].label == 'Пароль (повторно)')

    def test_password2_form_field_widgets_False(self):
        self.assertFalse(self.form.fields['password2'].widget == forms.PasswordInput)

    def test_password2_form_field_help_text_True(self):
        self.assertTrue(self.form.fields['password2'].help_text == 'Введите тот же самый пароль еще раз для проверки')

    def test_password1_checked_Null_KeyError(self):
        password1 = ''
        password2 = 'mikipiki123'
        form_password = {'password1': password1, 'password2': password2}
        form = RegisterUserForm(data=form_password)
        self.assertRaises(KeyError)

    def test_password2_checked_Null_KeyError(self):
        password1 = 'mikipiki123'
        password2 = ''
        form_password = {'password1': password1, 'password2': password2}
        form = RegisterUserForm(data=form_password)
        self.assertRaises(KeyError)

    def test_password1_and_password2_checked_Null_KeyError(self):
        password1 = ''
        password2 = ''
        form_password = {'password1': password1, 'password2': password2}
        form = RegisterUserForm(data=form_password)
        self.assertRaises(KeyError)

    def test_password1_and_password2_is_not_equals_KeyError(self):
        password1 = 'mikipiki123'
        password2 = 'mikipiki1234'
        form_password = {'password1': password1, 'password2': password2}
        form = RegisterUserForm(data=form_password)
        self.assertRaises(KeyError)

    def test_password1_and_password2_is_equals(self):
        password1 = 'mikipiki123'
        password2 = 'mikipiki123'
        form_password = {'password1': password1, 'password2': password2}
        form = RegisterUserForm(data=form_password)
        self.assertRaises(KeyError)
