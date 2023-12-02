from django.shortcuts import render
from django.views.generic import View
from .models import *

# Create your views here.
class IndexView(View):
    def get(self, request):
        guitars = Guitarra.objects.filter(color = 'Silver')[0:3]
        print(guitars)

        return render(request, "index.html", {'guitars': guitars})
