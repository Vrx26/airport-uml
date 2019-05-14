from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.forms.widgets import SelectDateWidget, EmailInput


class SearchForm(forms.Form):
    departure_time = forms.DateField(label='Дата вылета:', widget=SelectDateWidget)
    departure_place = forms.CharField(label='Откуда:', max_length=100)
    arrival_place = forms.CharField(label='Куда:', max_length=100)


class OrderForm(forms.Form):
    CHOICES = [('0', 'Эконом класс'),
               ('1', 'Бизнес класс')]

    place_type = forms.ChoiceField(label='Тип места:', choices=CHOICES, widget=forms.RadioSelect)
    amount = forms.IntegerField(label='Количество мест:', widget=forms.NumberInput, initial=1)

    luggage_amount = forms.IntegerField(label='Количество мест с багажом:', widget=forms.NumberInput, initial=0)  # TODO validator
    children_amount = forms.IntegerField(label='Количество мест для детей:', widget=forms.NumberInput, initial=0)  # TODO validator


class CustomUserCreationForm(UserCreationForm):
    last_name = forms.CharField(label='Фамилия')
    first_name = forms.CharField(label='Имя')
    second_name = forms.CharField(label='Отчество')
    passport_series = forms.CharField(label='Серия паспорта')
    passport_number = forms.CharField(label='Номер паспорта')


    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email',
                  'passport_series', 'last_name',
                  'first_name', 'passport_number',
                  'second_name')


class CustomUserChangeForm(UserChangeForm):
    passport_series = forms.CharField(label='Серия паспорта')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'passport_series')