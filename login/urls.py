from django.urls import path
from . import views

app_name = 'login'
urlpatterns =[
    path('',views.user_login,name = 'user_login'),
    path('logout/',views.logout,name = 'logout'),
    path('home/',views.home_page,name = 'home'),
    path('donate/',views.process_payment,name = 'donate'),
    path('payment_done/',views.payment_done,name = "payment_done"),
    path('payment_cancelled/',views.payment_canceled,name = "payment_cancelled"),
]