from rest_framework.serializers import ModelSerializer
from hotelaria.models.pagamento import Pagamento

class PagamentoSerializer(ModelSerializer):

    class Meta:
        model = Pagamento
        fields = "__all__"