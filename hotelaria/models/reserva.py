from django.db import models

class Reserva(models.Model):
    pk_idServicos = models.IntegerField(primary_key=True)
    nome_servico = models.CharField(max_length=45)

    def __str__(self):
        return self.nome_servico