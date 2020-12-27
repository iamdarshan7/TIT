from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class UniversitiesTemplateView(TemplateView):
    template_name = 'universities.html'

class UniversityTemplateView(TemplateView):
    template_name = 'university.html'

class SchoolsTemplateView(TemplateView):
    template_name = 'schools.html'

class SchoolTemplateView(TemplateView):
    template_name = 'school.html'

class CollegesTemplateView(TemplateView):
    template_name = 'colleges.html'

class CollegeTemplateView(TemplateView):
    template_name = 'college.html'

class MontessorisTemplateView(TemplateView):
    template_name = 'montessoris.html'

class MontessoriTemplateView(TemplateView):
    template_name = 'montessori.html'

class TutionCentersTemplateView(TemplateView):
    template_name = 'tution_centers.html'

class TutionCenterTemplateView(TemplateView):
    template_name = 'tution_center.html'

class TrainingCentersTemplateView(TemplateView):
    template_name = 'training_centers.html'

class TrainingCenterTemplateView(TemplateView):
    template_name = 'training_center.html'