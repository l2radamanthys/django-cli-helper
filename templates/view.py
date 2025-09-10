from rest_framework import viewsets
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
