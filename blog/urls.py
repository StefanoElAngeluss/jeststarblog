from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccueilView.as_view(), name='accueil'),
    path("<slug:article>/", views.article_single, name="article_single"),
]