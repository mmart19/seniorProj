"""seniorProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers, permissions
from biopath import views
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


router = routers.DefaultRouter()
router.register(r'pathways', views.PathWayViewSet)
router.register(r'modules', views.ModuleViewSet)
router.register(r'products', views.ProductsViewSet)
router.register(r'substrates', views.SubstratesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('biopath/', include('biopath.urls')),
    path('admin/', admin.site.urls),
]
