from django.db import models
from livros.models import Livro


# Create your models here.
class Emprestimo(models.Model):
    livro = models.ForeignKey('Livro', on_delete=models.CASCADE)
    