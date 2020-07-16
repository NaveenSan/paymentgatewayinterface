from django.urls import path
from . import views
#app name to locate
app_name = 'dashboard'

urlpatterns = [
    #dash board with few info
    path('',views.front_page,name = 'front_page'),
]