from rest_framework.serializer import ModelSerializer
from hotelaria.models.reserva_servico import Reserva_servico

class Reserva_servicoSerializer(ModelSerializer):
    class Meta:
        model = Reserva_servico
        fields = '__all__'