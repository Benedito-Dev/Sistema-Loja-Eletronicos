from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email