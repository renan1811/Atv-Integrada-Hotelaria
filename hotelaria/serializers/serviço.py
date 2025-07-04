from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from hotelaria.models import Serviço

class ServiçoSerializer(ModelSerializer):    
    class Meta:
        model = Serviço
        read_only_fields = ["idServico",]
        fields = ["idServico", "nome_Servico"]