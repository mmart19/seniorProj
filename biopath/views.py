from django.shortcuts import render
from django.http import HttpResponse
from biopath.models import Pathway, Module, Products, Substrates
from biopath.serializers import PathwaySerializer, ModuleSerializer, ProductsSerializer, SubstratesSerializer
from rest_framework import viewsets

# Create your views here.
def index(request):
      return HttpResponse("Hello world from django backend")

#Views that handle the HTTP requests for models
class PathWayViewSet(viewsets.ModelViewset):
      queryset = Pathway.objects.all()
      serializer_class = PathwaySerializer

class ModuleViewSet(viewsets.ModelViewset):
      queryset = Module.objects.all()
      serializer_class = ModuleSerializer

class ProductsViewSet(viewsets.ModelViewset):
      queryset = Products.objects.all()
      serializer_class = ProductsSerializer

class SubstratesViewSet(viewsets.ModelViewset):
      queryset = Substrates.objects.all()
      serializer_class = SubstratesSerializer

      
