from django.urls import path
from thisApp import views

urlpatterns = [
    path('', views.index, name='index')
]
