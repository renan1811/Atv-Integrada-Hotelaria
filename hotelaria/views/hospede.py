from rest_framework.viewsets import ModelViewSet

from hotelaria.serializers.hospede import HospedeSerializer
from hotelaria.models.hospede import Hospede

class HospedeViewSet(ModelViewSet):
    queryset = Hospede.objects.all()
    serializer_class = HospedeSerializer
