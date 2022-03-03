from msilib import schema
from django.shortcuts import render
from django.http import HttpResponse
from biopath.models import Pathway, Module, Products, Substrates
from biopath.serializers import PathwaySerializer, ModuleSerializer, ProductsSerializer, SubstratesSerializer
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer



# Create your views here.
def index(request):
      return HttpResponse("Hello world from django backend")

#Views that handle the HTTP requests for models
# These are only used to view data

class PathWayViewSet(viewsets.ModelViewSet):
      queryset = Pathway.objects.all()
      serializer_class = PathwaySerializer

class ModuleViewSet(viewsets.ModelViewSet):
      queryset = Module.objects.all()
      serializer_class = ModuleSerializer

class ProductsViewSet(viewsets.ModelViewSet):
      queryset = Products.objects.all()
      serializer_class = ProductsSerializer

class SubstratesViewSet(viewsets.ModelViewSet):
      queryset = Substrates.objects.all()
      serializer_class = SubstratesSerializer


# These views are used for API documentation
class PathwayList(generics.ListCreateAPIView):
      queryset = Pathway.objects.all()
      serializer_class = PathwaySerializer

class PathwayDetail(generics.RetrieveUpdateDestroyAPIView):
      queryset = Pathway.objects.all()
      serializer_class = PathwaySerializer

class SubstratesList(generics.ListCreateAPIView):
      queryset = Substrates.objects.all()
      serializer_class = SubstratesSerializer

class SubstratesDetail(generics.RetrieveUpdateDestroyAPIView):
      queryset = Substrates.objects.all()
      serializer_class = SubstratesSerializer



      
