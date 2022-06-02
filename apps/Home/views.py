from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class Home(LoginRequiredMixin,TemplateView):
    login_url="/auth/login"
    template_name = 'Home/landing.html'
