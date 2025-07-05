from rest_framework.serializers import ModelSerializer
from hotelaria.models.quarto import Quarto

class QuartoSerializer(ModelSerializer):
    
    class Meta:
        model = Quarto
        fields = '__all__'