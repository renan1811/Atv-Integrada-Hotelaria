from django.db import models
from .serviço import Serviço
from .reserva import Reserva

class Reserva_servico(models.Model):
    servico = models.ForeignKey(Serviço, on_delete=models.CASCADE)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.servico}, {self.reserva}"