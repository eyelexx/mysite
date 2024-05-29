from django.db import models # Ferramentas necessárias para definir os modelos de banco de dados.
from django.contrib.auth.models import User # Modelo de usuário padrão do Django.


# Define as opções de status de um post.
STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

# Modelo de banco de dados.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    update_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # Metadados do modelo.
    class Meta:
        ordering = ['-created_on'] # Ordenacao em ordem decrescente por padrão.

    # Define a representacao em string do objeto 'Post', que neste caso é o título do post.
    def __str__(self):
        return self.title