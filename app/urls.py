from . import views
from django.urls import path


urlpatterns = [
    # path('', views.hello, name='hello'),
    path('', views.add_data, name='add'),
    # path('program-data/', views.get_program_data, name='program-data'),
    # path('percentage-data/', views.get_percentage_data, name='percentage-data'),
]
