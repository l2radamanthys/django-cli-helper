from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from rest_framework_json_api.relations import ResourceRelatedField

from %nombre_app%.models.perfil import %modelo%


class %modelo%Serializer(ModelSerializer):
    class Meta:
        model = %modelo%
        fields = (
            'nombre',
        )

    # included_serializers = {
    #     'user': UserSerializer,
    # }
