from rest_framework import viewsets

from aplicacion.models.modelo import SerieAnime
from aplicacion.serializers.modelo import SerieAnimeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class SerieAnimeViewSet(viewsets.ModelViewSet):
    queryset = SerieAnime.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = SerieAnimeSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
