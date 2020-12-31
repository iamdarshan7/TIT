from django.urls import path 
from . import views


urlpatterns = [
    path('australia/', views.AustraliaTemplateView.as_view(), name='australia'),
    path('usa/', views.UsaTemplateView.as_view(), name='usa'),
    path('india/', views.IndiaTemplateView.as_view(), name='india'),
    path('germany/', views.GermanyTemplateView.as_view(), name='germany'),
    path('canada/', views.CanadaTemplateView.as_view(), name='canada'),
]