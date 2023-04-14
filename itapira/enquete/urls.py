#importando a função path
from django.urls import path
#enchergando o arquivo views
from . import views
#
urlpatterns = [
    path('', views.index, name='index'),
    path('valkor', views.valkor, name='valkor')
]