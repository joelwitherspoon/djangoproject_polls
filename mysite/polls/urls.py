""" Local app urls """

from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [

    # index
    path('',views.index, name = 'index'),
]
