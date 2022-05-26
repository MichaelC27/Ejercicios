from django.urls import  path
from . import views

urlpatterns = [
     path('directores/',views.index, name='index')
]
