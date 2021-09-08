from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from %app%.models.%nombre_archivo% import %modelo%
from %app%.serializers.%nombre_archivo% import %modelo%Serializer


class %modelo%ViewSet(viewsets.ModelViewSet):
    queryset = %modelo%.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = %modelo%Serializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
