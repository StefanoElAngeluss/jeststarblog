from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .models import Article

class AccueilView(ListView):
  model = Article
  context_object_name = "articles"
  paginate_by = 10

  def get_template_names(self):
    if self.request.htmx:
      return 'blog/components/article_liste_elements.html'
    return 'pages/accueil.html'

def article_single(request, article):
  article = get_object_or_404(Article, slug=article, status="publier")
  return render(request, 'pages/article_single.html', {
    'article': article
  })