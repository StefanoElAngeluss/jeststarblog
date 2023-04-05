from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccueilView.as_view(), name='accueil'),
]