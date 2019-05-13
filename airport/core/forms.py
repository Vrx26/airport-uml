from django import forms
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

    last_name = forms.CharField(label='Фамилия', max_length=100)
    name = forms.CharField(label='Имя', max_length=100)
    second_name = forms.CharField(label='Отчество', max_length=100)
    passport_series = forms.IntegerField(label='Серия паспорта')
    passport_number = forms.IntegerField(label='Номер паспорта')
    email = forms.CharField(label='email', widget=EmailInput)

