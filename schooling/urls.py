from django.urls import path
from . import views

urlpatterns = [
    path('universities/', views.UniversitiesTemplateView.as_view(), name='universities'),
    path('universities/1/', views.UniversityTemplateView.as_view(), name='university'),
    path('schools/', views.SchoolsTemplateView.as_view(), name='schools'),
    path('schools/1/', views.SchoolTemplateView.as_view(), name='school'),
    path('colleges/', views.CollegesTemplateView.as_view(), name='colleges'),
    path('colleges/1/', views.CollegeTemplateView.as_view(), name='college'),
    path('montessori/', views.MontessorisTemplateView.as_view(), name='montessoris'),
    path('montessori/1/', views.MontessoriTemplateView.as_view(), name='montessori'),
    path('Training_centers/', views.TrainingCentersTemplateView.as_view(), name='training_centers'),
    path('Training_centers/1/', views.TrainingCenterTemplateView.as_view(), name='training_center'),
    path('Tution_centers/', views.TutionCentersTemplateView.as_view(), name='tution_centers'),
    path('Tution_centers/1/', views.TutionCenterTemplateView.as_view(), name='tution_center'),
]