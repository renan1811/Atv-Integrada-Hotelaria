from django.db import models

class Pagamento(models.Model):
    valor_pagamento = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()



    def __str__(self):
        return f"R${self.valor_pagamento} ({self.data_pagamento})"