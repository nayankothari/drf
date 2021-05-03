from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import DataModel
from .serializers import DataSerializers
# Create your views here.


class ListDisplay(ListCreateAPIView):
    queryset = DataModel.objects.all()
    serializer_class = DataSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class RetriveData(RetrieveUpdateDestroyAPIView):
    queryset = DataModel.objects.all()
    serializer_class = DataSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
