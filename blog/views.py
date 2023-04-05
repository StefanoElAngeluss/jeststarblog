from django.shortcuts import render
from django.views.generic import ListView
from .models import Article

class AccueilView(ListView):
  model = Article
  template_name = 'blog/accueil.html'
  context_object_name = 'articles'