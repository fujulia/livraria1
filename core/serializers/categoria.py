# from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ModelSerializer

from core.models import Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
        # permission_classes = [IsAuthenticated]