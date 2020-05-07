""" Local app urls """

from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [

    # index
    path('', views.IndexView.as_view(), name='index'),

    # detail
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # vote
    path('<int:question_id>/vote/', views.vote, name='vote'),



]
