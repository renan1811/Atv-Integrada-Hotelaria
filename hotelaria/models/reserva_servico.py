from django.db import models

class Reserva_servico(models.Model):
    servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.servico}, {self.reserva}"