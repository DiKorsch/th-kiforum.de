from rest_framework import viewsets
from api.models import Demonstrator
from api.serializers import DemonstratorSerializer



class DemonstratorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Demonstrator.objects.all()
    serializer_class = DemonstratorSerializer
