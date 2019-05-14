from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('flight/<str:id>/', views.flight_registration),
    path('orders', views.orders, name='orders'),
    path('register', views.SignUp.as_view(), name='signup'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]