from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('flight/<str:id>/', views.flight_registration),
]