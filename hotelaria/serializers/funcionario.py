from rest_framework.serializers import ModelSerializer
from hotelaria.models import Funcionario

class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'