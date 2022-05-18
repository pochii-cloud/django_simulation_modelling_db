from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class HomeView(View):
    def get(self, request):
        return HttpResponse('Welcome to simulation and modelling')

    def post(self, request):
        return HttpResponse('Welcome to simulation and modelling')
