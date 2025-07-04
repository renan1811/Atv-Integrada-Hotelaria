from rest_framework.viewsets import ModelViewSet

from hotelaria.serializers.pagamento import PagamentoSerializer
from hotelaria.models.pagamento import Pagamento

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
