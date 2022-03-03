from django.urls import path
from biopath import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
      path('', views.SubstratesList.as_view()),
      path('<int:pk>/', views.SubstratesDetail.as_view()),
]

