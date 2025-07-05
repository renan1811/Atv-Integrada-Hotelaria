from django.db import models

class Funcionario(models.Model):
    idFuncionario = models.IntegerField(primary_key=True)
    email_funcionario = models.CharField(max_length=45)
    salario_funcionario = models.DecimalField(max_digits=7, decimal_places=2)
    Servicos_pk_idServicos = models.IntegerField()

    def __str__(self):
        return self.email_funcionario