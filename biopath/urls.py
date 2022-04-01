from django.urls import path
from biopath import views

urlpatterns = [
      path('', views.SubstratesList.as_view()),
      path('<int:pk>/', views.SubstratesDetail.as_view()),
]

