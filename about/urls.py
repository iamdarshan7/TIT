from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.AboutUsTemplateView.as_view(), name='about_us'),
    path('promise/', views.PromiseTemplateView.as_view(), name='promise'),
    path('event/', views.EventTemplateView.as_view(), name='event'),
    path('announcement/', views.AnnouncementTemplateView.as_view(), name='announcement'),
]