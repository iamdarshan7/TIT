from . import views
from django.urls import path


urlpatterns = [
    # path('', views.hello, name='hello'),
    path('', views.add_data, name='add'),
    # path('another/', views.add_another_data, name="add_another"),
    path('contact/', views.Contact.as_view(), name="contact_page"),
    # path('program-data/', views.get_program_data, name='program-data'),
    # path('percentage-data/', views.get_percentage_data, name='percentage-data'),
]
