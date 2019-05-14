from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import SearchForm, OrderForm, CustomUserCreationForm
from .models import Flight, Place, Order, CustomUser

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

    if request.method == 'POST':  # process user data
        form = OrderForm(request.POST)
        if form.is_valid():
            if type == '0':
                sum = form.cleaned_data['amount'] * econom.price + form.cleaned_data['luggage_amount'] * econom.luggage_price + form.cleaned_data['children_amount'] * econom.children_price
            else:
                sum = form.cleaned_data['amount'] * business.price + form.cleaned_data['luggage_amount'] * business.luggage_price + form.cleaned_data['children_amount'] * business.child_place_price

            data = {'type': form.cleaned_data['place_type'],
                    'amount': form.cleaned_data['amount'],
                    'luggage_amount': form.cleaned_data['luggage_amount'],
                    'children_amount': form.cleaned_data['children_amount'],
                    'sum': sum}

            if data['type'] == '0':
                place = econom
            else:
                place = business

            if check_payment() and place.free_places >= data['amount']:

                user = request.user
                print(user.id)

                # decreasing amount of free places
                place.free_places -= data['amount']
                place.save()

                order = Order(customer=user,
                              place=place,
                              order_sum=data['sum'])
                order.save()

                send_email(data)
                return render(request, 'thanks.html')
            else:
                return render(request, 'Error.html')

    else:  # render form for user
        form = OrderForm()
        return render(request, 'flight_info.html', {'form':form, 'flight': flight, 'econom': econom, 'business':business, 'title': id})


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register_user.html'


def orders(request):

    orders_list={}

    return render(request, 'orders.html', {'orders': orders_list})
