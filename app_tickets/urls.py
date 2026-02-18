from django.urls import path
from . import views

app_name = 'app_tickets'

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),
]
