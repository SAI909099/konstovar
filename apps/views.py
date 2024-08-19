from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from apps.forms import RegisterForm


class HomepageTemplateView(TemplateView):
    template_name = 'apps/index.html'


class RegisterFormView(FormView):
    template_name = "apps/auth/register.html"
    form_class = RegisterForm

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return redirect('login')