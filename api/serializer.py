from rest_framework import serializers
from .models import User, ServiceRequirements, Services, DetailRequirements, Arrangement, FileRequirement


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ServiceRequirementsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceRequirements
        fields = '__all__'


class ServicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class DetailRequirementsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DetailRequirements
        fields = '__all__'


class ArrangementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Arrangement
        fields = '__all__'


class FileRequirementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileRequirement
        fields = '__all__'
