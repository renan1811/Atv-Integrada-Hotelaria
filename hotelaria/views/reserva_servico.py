from rest_framework.viewsets import ModelViewSet
from hotelaria.models.reserva_servico import Reserva_servico
from hotelaria.serializers.reserva_servico import Reserva_servicoSerializer

class Reserva_servicoViewSet(ModelViewSet):
    queryset = Reserva_servico.objects.all()
    serializer_class = Reserva_servicoSerializer