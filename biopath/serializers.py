from pathlib import Path
from rest_framework_json_api import serializers
from biopath.models import Pathway, Module, Products, Substrates

class PathwaySerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
            model = Pathway
            fields = ('modelName', 'id')

class ModuleSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
            model = Module
            fields = ('enzyme', 'enzymeAbbr', 'reversible', 'xCoor', 'yCoor')

class ProductsSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
            model = Products
            fields = ('product', 'abbr')

class SubstratesSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
            model = Substrates
            fields = ('substrate', 'abbr')