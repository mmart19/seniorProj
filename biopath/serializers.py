from pathlib import Path
from rest_framework_json_api import serializers
from biopath.models import Pathway, Module, Products, Substrates

class PathwaySerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
            model = Pathway
            fields = ('modelName', 'id')
      
      # Method used to create new pathway objects to be stored into SQL database
      def create(self, validated_data):
            return Pathway.objects.create(** validated_data)
      
      #Serializes python data into JSON format
      def update(self, instance, validated_data):
            instance.modelName = validated_data.get('modelName', instance.modelName)
            instance.save()
            return instance

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


