import factory
from django.contrib.auth.models import User
from factory.faker import faker

from .models import Article

FAKE = faker.Faker()

class ArticleFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Article

  titre = factory.Faker('sentence', nb_words=12)
  sous_titre = factory.Faker('sentence', nb_words=12)
  slug = factory.Faker('slug')
  auteur = User.objects.get_or_create(username='stefano')[0]

  @factory.lazy_attribute
  def contenu(self):
    x = ''
    for _ in range(0,5):
      x += '\r\n' + FAKE.paragraph(nb_sentences=30) + '\r\n'
    return x

  status = 'published'

  @factory.post_generation
  def tags(self, create, extracted, **kwargs):
    if not create:
      return

    if extracted:
      self.tags.add(extracted)
    else:
      self.tags.add(
        "Back-End",
        "Deployment",
        "Développement",
        "Django",
        "Database",
        "Front-End",
        "Javascript",
        "ORM",
        "Pytest",
        "Python",
        "Ruby on Rails"
        "VSCode",
      )