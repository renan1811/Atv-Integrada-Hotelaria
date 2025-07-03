from django.db import models

class Hospede(models.Model):
    CPF = models.IntegerField(unique=True)
    data_nascimento_hospede = models.DateField()
    login_hospede = models.CharField(max_length=50, unique=True)
    senha_hospede = models.CharField(max_length=50)
    email_hospede = models.EmailField(max_length=254, unique=True)
    nome_hospede = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome_hospede}"