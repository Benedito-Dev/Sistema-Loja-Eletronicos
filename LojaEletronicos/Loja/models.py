from django.db import models
from django.contrib.auth.models import AbstractUser

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quant = models.IntegerField()
    categoria = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class CustomUSer(AbstractUser):
    CPF = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    telefone = models.CharField(15)
    cargo = models.CharField(100)
    