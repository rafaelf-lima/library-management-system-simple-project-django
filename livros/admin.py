from django.contrib import admin
from .models import Autor, Livro, Genero
# Register your models here.
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano_publicacao', 'genero', 'disponivel')
    search_fields = ('titulo', 'autor', 'genero', 'ano_publicacao')
    list_filter = ('disponivel', 'genero', 'ano_publicacao')

admin.site.register(Autor)
admin.site.register(Genero)
