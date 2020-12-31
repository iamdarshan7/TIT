from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class AboutUsTemplateView(TemplateView):
    template_name = 'about_us.html'

class PromiseTemplateView(TemplateView):
    template_name = 'promise.html'    

class EventTemplateView(TemplateView):
    template_name = 'event.html'

class AnnouncementTemplateView(TemplateView):
    template_engine = 'announcement.html'    
