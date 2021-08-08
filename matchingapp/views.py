from django.shortcuts import render

# Create your views here.
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import CountrySerializer,ClubSerializer,PlayerSerializer,MembershipSerializer
from .models import Club,Country,Player,Membership
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser

class CountryViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]
    
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    # filter_fields = ('name',)
    
    def post(self, request, format=None):
        serializer = CountrySerializer(data=request.data, instance=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClubViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]
    
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('country__name','club_membership__player__name','name')

    def post(self, request, format=None):
        serializer = ClubSerializer(data=request.data, instance=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlayerViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    # filter_fields = ('player__country__name',)

    def post(self, request, format=None):
        serializer = PlayerSerializer(data=request.data, instance=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MembershipViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]

    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('club__name')
    filter_fields = ('player__country__name',)


    def post(self, request, format=None):
        serializer = MembershipSerializer(data=request.data, instance=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


