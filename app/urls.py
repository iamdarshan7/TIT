from . import views
from django.urls import path


urlpatterns = [
    # path('', views.hello, name='hello'),
    path('', views.add_data, name='add'),
]
