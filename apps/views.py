from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView


class HomepageTemplateView(TemplateView):
    template_name = 'apps/index.html'
