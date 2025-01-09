from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quant = models.IntegerField()
    categoria = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)

    def __str__(self):
        return self.nome