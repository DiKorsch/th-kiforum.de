from rest_framework import serializers
from api.models import Demonstrator

class DemonstratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demonstrator
        fields = '__all__'
        depth = 1
