from django.urls import path
from . import views

urlpatterns = [
    path('',views.vista_calidad_aire, name='index'),
    path('data/', views.CalidadAireList.as_view(), name='calidadaire-list'),
    path('data/<int:pk>/', views.CalidadAireDetail.as_view(), name='calidadaire-detail'),
]
