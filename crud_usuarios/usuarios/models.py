from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    idade = models.IntegerField()

    def __str__(self) -> str:
        return self.nome