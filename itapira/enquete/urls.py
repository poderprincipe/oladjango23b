#importando a função path
from dango.urls import paht
#enchergando o arquivo views
from . import views
#
urlpatterns + [
    paht('', views.index, name='index')
]