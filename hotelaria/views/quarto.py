from rest_framework.viewsets import ModelViewSet
from hotelaria.models.quarto import Quarto
from hotelaria.serializers.quarto import QuartoSerializer

class QuartoViewSet(ModelViewSet):
    queryset = Quarto.objects.all()
    serializer_class = QuartoSerializer



