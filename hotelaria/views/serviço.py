from rest_framework.viewsets import ModelViewSet

from hotelaria.serializers.serviço import ServiçoSerializer
from hotelaria.models.serviço import Serviço

class ServiçoViewSets(ModelViewSet):
    queryset = Serviço.objects.all()
    serializer_class = ServiçoSerializer
