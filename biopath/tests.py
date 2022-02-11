from ast import Mod
from itertools import product
from django.test import TestCase, Client
from .models import Pathway, Products, Substrates, Module

# Create your tests here.

class SimpleTest(TestCase):
      def setUp(self):
            self.test_client = Client()

      def test_response(self):
            response = self.test_client.get('/biopath/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content, b"Hello world from django backend")

class DataTest(TestCase):
      def setUp(self):
            Pathway1 = Pathway.objects.create(id=1, userID=1, modelName="Glycolysis", public=False)
            Product1 = Products.objects.create(id=1, product="Adenosine Triphosphate", abbr="ATP", ModelID=1, ModuleID_id=1)
            Substrate1 = Substrates.objects.create(id=1, Substrate="Hexokinase", abbr="HK", modelID="1", moduleID_id="1")
            Module1 = Module.objects.create(id=1, enzyme="Adenosine Diphosphate", enzymeAbbr="ADP", reversible="reversible", xCoor=1.0, yCoor=1.0, enzWeight=1.0, deltaG=-1.0, deltaGNaughtPrime=1.0, modelID_id=1)
      
      def test_objects(self):
            pathways = Pathway.objects.all()
            products = Products.objects.all()
            substrates = Substrates.objects.all()
            modules = Module.objects.all()

            self.assertEqual(len(pathways), 1)
            self.assertEqual(len(products), 1)
            self.assertEqual(len(substrates), 1)
            self.assertEqual(len(modules), 1)

            
