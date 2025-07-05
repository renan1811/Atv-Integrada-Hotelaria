from django.db import models
import uuid

class Serviço(models.Model):
    idServico = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    nome_Servico = models.CharField(max_length=45)

