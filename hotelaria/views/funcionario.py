from rest_framework.viewsets import ModelViewSet

from hotelaria.serializers.funcionario import FuncionarioSerializer
from hotelaria.models.funcionario import Funcionario


class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer