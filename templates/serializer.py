from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from %app%.models.%nombre_archivo% import %modelo%


class %modelo%Serializer(ModelSerializer):
    class Meta:
        model = %modelo%
        fields = (
            'id',
            'nombre',
        )

