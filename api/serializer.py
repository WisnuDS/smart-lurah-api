from rest_framework import serializers
from .models import User, ServiceRequirements, Services, DetailRequirements, Arrangement, FileRequirement


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ServiceRequirementsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceRequirements
        fields = ['url','id','name_requirement']


class ServicesSerializer(serializers.HyperlinkedModelSerializer):
    detail = serializers.StringRelatedField(many=True,read_only=True)

    class Meta:
        model = Services
        fields = ['id','url','type_service','status','detail']


class DetailRequirementsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DetailRequirements
        fields = '__all__'


class ArrangementSerializer(serializers.HyperlinkedModelSerializer):
    file_requirement = serializers.StringRelatedField(many=True,read_only=True)

    class Meta:
        model = Arrangement
        fields = ['id','url','user','service','date','status','file_requirement']


class FileRequirementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileRequirement
        fields = '__all__'
