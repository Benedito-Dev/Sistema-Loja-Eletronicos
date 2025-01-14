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
    
class CustomUser(AbstractUser):
    CPF = models.CharField(max_length=11, default=12345678910)
    endereco = models.CharField(max_length=100, default="rua topazio")
    salario = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    telefone = models.CharField(max_length=15, default=85986475337)
    cargo = models.CharField(max_length=100, default="empregado")
    