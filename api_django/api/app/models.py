from django.db import models

# Create your models here.
class Receita(models.Model):
    nome = models.CharField(max_length=150)
    # outras_informacoes = models.CharField(max_length=250)

# class Ingrediente(models.Model):
#     nome = models.CharField(max_length=150)

class ModoPreparo(models.Model):
    passos = models.CharField(max_length=500)
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)

class IngredienteReceita(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    ingrediente = models.CharField(max_length=250)
    # ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    # quantidade_ingrediente = models.IntegerField(default=0)

class InformacaoReceita(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    informacao = models.CharField(max_length=250)
