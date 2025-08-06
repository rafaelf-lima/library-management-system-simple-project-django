from django.db import models

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    ano_publicacao = models.IntegerField()
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE)
    resumo = models.TextField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField()

    def __str__(self):
        return self.nome
    
class Genero(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome