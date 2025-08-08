from datetime import timedelta, timezone
from django.conf import settings
from django.db import models
from livros.models import Livro


# Create your models here.
class Emprestimo(models.Model):

    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('ATRASADO', 'Atrasado'),
        ('DEVOLVIDO', 'Devolvido'),
    ]

    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField()
    data_devolucao_real = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDENTE')

    def save(self, *args, **kwargs):
        if not self.pk and not self.data_devolucao:
            self.data_devolucao = timezone.now().date() + timedelta(days=14)
        super().save(*args, **kwargs)

        
    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"
        ordering = ['-data_emprestimo']

    def __str__(self):
        return f"{self.livro.titulo} emprestado para {self.usuario.username}"

    
    