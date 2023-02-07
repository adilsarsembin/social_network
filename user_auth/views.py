from django.shortcuts import render
from django.views import View

# Create your views here.

class UserView(View):
    def get(self, request):
        print('qe')