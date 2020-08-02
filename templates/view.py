from rest_framework import viewsets

from aplicacion.models.modelo import %modelo%
from aplicacion.serializers.modelo import %modelo%Serializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class %modelo%ViewSet(viewsets.ModelViewSet):
    queryset = %modelo%.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = %modelo%Serializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
