from django.urls import path, include, 
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pathways', views.PathWayViewSet)
router.register(r'modules', views.ModuleViewSet)
router.register(r'products', views.ProductsViewSet)
router.register(r'substrates', views.SubstratesViewSet)

urlpatterns = [
      path('', include(router.urls)),
]