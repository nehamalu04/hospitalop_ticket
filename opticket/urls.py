from django.urls import path
from . import views

urlpatterns = [
    path('', views.op_ticket_view, name='op_ticket'),
    
]



































