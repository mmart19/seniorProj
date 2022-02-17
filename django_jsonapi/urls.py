from django.urls import include, pathlib
from rest_framework import routers
from biopath import views

router = routers.DefaultRouter()
router.register(r'pathways', views.PathWayViewSet)
router.register(r'modules', views.ModuleViewSet)
router.register(r'products', views.ProductsViewSet)
router.register(r'substrates', views.SubstratesViewSet)

urlpatterns = [
      path('', include(router.urls)),
]