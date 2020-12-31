from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class UsaTemplateView(TemplateView):
    template_name = 'usa.html'


class CanadaTemplateView(TemplateView):
    template_name = 'canada.html'

class GermanyTemplateView(TemplateView):
    template_name = 'germany.html'

class AustraliaTemplateView(TemplateView):
    template_name = 'australia.html'

class IndiaTemplateView(TemplateView):
    template_name = 'india.html'