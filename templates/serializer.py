from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
# from rest_framework_json_api.relations import ResourceRelatedField

from %app%.models.%nombre_archivo% import %modelo%


class %modelo%Serializer(ModelSerializer):
    class Meta:
        model = %modelo%
        fields = (
            'id',
            'nombre',
        )

    # included_serializers = {
    #     'user': UserSerializer,
    # }
