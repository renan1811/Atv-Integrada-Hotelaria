from rest_framework.serializer import ModelSerializer
from hotelaria.models.reserva import Reserva

class ReservaSerializer(ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'