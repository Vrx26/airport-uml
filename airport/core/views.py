from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import SearchForm, Order
from .models import Flight, Place

# Create your views here.


def check_payment():
    return True


def send_email(data):
    pass  # TODO


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            departure_date=form.cleaned_data.get('departure_time')
            departure_place=form.cleaned_data['departure_place']
            arrival_place = form.cleaned_data['arrival_place']

            flights = Flight.objects.filter(departure_time__year=departure_date.year,
                                            departure_time__month=departure_date.month,
                                            departure_time__day=departure_date.day,
                                            departure_place__city=departure_place,
                                            arrival_place__city=arrival_place)
            return render(request, 'result.html', {'flights': flights, 'title': 'Результат'})
    else:
        form = SearchForm()
        return render(request, 'search.html', {'form': form, 'title': 'Поиск'})


def flight_registration(request, id):

    flight = Flight.objects.get(flight_id=id)
    places = Place.objects.filter(flight=flight)
    for place in places:
        if place.place_type == 0:
            econom = place
        elif place.place_type == 1:
            business = place

    if request.method == 'POST':
        form = Order(request.POST)
        if form.is_valid():
            if type == '0':
                sum = form.cleaned_data['amount'] * econom.price + form.cleaned_data['luggage_amount'] * econom.luggage_price + form.cleaned_data['children_amount'] * econom.children_price
            else:
                sum = form.cleaned_data['amount'] * business.price + form.cleaned_data['luggage_amount'] * business.luggage_price + form.cleaned_data['children_amount'] * business.child_place_price

            data = {'type': form.cleaned_data['place_type'],
                    'amount': form.cleaned_data['amount'],
                    'luggage_amount': form.cleaned_data['luggage_amount'],
                    'children_amount': form.cleaned_data['children_amount'],
                    'sum': sum,
                    'last_name': form.cleaned_data['last_name'],
                    'name': form.cleaned_data['name'],
                    'second_name': form.cleaned_data['second_name'],
                    'series': form.cleaned_data['passport_series'],
                    'number': form.cleaned_data['passport_number'],
                    'email': form.cleaned_data['email']}

            if check_payment():
                send_email(data)
                return render(request, 'thanks.html')
            else:
                return render(request, 'Error.html')


    else:
        form = Order()
        return render(request, 'flight_info.html', {'form':form, 'flight': flight, 'econom': econom, 'business':business, 'title': id})
