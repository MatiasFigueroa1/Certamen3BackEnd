from rest_framework import serializers
from .models import Auto
from .models import Marca

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = "__all__"

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"