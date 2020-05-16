from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.parsers import BaseParser,JSONParser
from rest_framework.decorators import parser_classes


# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import User, ServiceRequirements, Services, DetailRequirements, Arrangement, FileRequirement
from api.serializer import UserSerializer, ServiceRequirementsSerializer, ServicesSerializer, \
    DetailRequirementsSerializer, ArrangementSerializer, FileRequirementSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer


class ServiceRequirementsViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequirements.objects.all()
    serializer_class = ServiceRequirementsSerializer


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class DetailRequirementViewSet(viewsets.ModelViewSet):
    queryset = DetailRequirements.objects.all()
    serializer_class = DetailRequirementsSerializer


class ArrangementViewSet(viewsets.ModelViewSet):
    queryset = Arrangement.objects.all()
    serializer_class = ArrangementSerializer


class FileRequirementViewSet(viewsets.ModelViewSet):
    queryset = FileRequirement.objects.all()
    serializer_class = FileRequirementSerializer


class PlainTextParser(BaseParser):
    """
    Plain text parser.
    """
    media_type = 'text/plain'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Simply return a string representing the body of the request.
        """
        return stream.read()


@api_view(('POST', 'GET'))
@parser_classes((PlainTextParser, JSONParser))
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    print(request.method)
    users = authenticate(username=username,password=password)
    if users is not None:
        data = {
            'id':users.id,
            'username': users.username,
            'email': users.email,
            'firstName':users.first_name,
            'lastName':users.last_name,
            'status': users.is_staff
        }
        return Response(data=data)
    else:
        data = {
            'status': False,
        }
        return Response(data=data)


@api_view(('POST', 'GET'))
@parser_classes((PlainTextParser, JSONParser))
def check_register(request):
    telegram_id = request.data.get('telegram_id')
    print(request.method)
    print(telegram_id)
    user = User.objects.filter(telegram_id=telegram_id)
    print(user)
    if user.exists():
        data = {
            'status': True,
        }
        return Response(data=data)
    else:
        data = {
            'status': False,
        }
        return Response(data=data)