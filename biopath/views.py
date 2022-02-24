from django.shortcuts import render
from django.http import HttpResponse
from biopath.models import Pathway, Module, Products, Substrates
from biopath.serializers import PathwaySerializer, ModuleSerializer, ProductsSerializer, SubstratesSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer


# Create your views here.
def index(request):
      return HttpResponse("Hello world from django backend")

#Views that handle the HTTP requests for models
class PathWayViewSet(viewsets.ModelViewSet):
      queryset = Pathway.objects.all()
      serializer_class = PathwaySerializer

      #@action(methods=['post'], detail=True)

class ModuleViewSet(viewsets.ModelViewSet):
      queryset = Module.objects.all()
      serializer_class = ModuleSerializer

class ProductsViewSet(viewsets.ModelViewSet):
      queryset = Products.objects.all()
      serializer_class = ProductsSerializer

class SubstratesViewSet(viewsets.ModelViewSet):
      queryset = Substrates.objects.all()
      serializer_class = SubstratesSerializer

      
