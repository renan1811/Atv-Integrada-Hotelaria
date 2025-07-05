from django.db import models

class Quarto(models.Model):
    num_quarto = models.IntegerField()
    andar_quarto = models.IntegerField()
    status_quarto = models.CharField(45)
    preço_diaria_quarto = models.DecimalField(max_digits=7, decimal_places=2) 
    
    def __str__(self):
        return f'Quarto: {self.num_quarto}'
    