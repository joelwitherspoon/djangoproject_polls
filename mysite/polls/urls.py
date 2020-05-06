""" Local app urls """

from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [

    # index
    path('', views.index, name='index'),

    # detail
    path('<int:question_id>/', views.detail, name='detail'),

    # results
    path('<int:question_id>/results/', views.results, name='results'),

    # vote
    path('<int:question_id>/vote/', views.vote, name='vote'),



]
