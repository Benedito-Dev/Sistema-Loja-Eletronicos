from django.db import models


class Produto(models.Model):
    id = models.AutoField(primary_key=True) 
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)  # Caminho da imagem no static
    
    def __str__(self):
        return self.nome
     #Retorna o nome do produto

    