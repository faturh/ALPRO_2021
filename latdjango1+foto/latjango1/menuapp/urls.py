from django.urls import path
from . import views

urlpatterns = [
    path('menuapp/', views.menuapp, name='menuapp'),
]