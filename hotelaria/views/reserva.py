from rest_framework.viewsets import ModelViewSet
from hotelaria.models.reserva import Reserva
from hotelaria.serializers.reserva import ReservaSerializer

class ReservaViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer