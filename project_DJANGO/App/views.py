from django.shortcuts import render
from django.views.generic import View
from .models import *

# Create your views here.
class IndexView(View):
    def get(self, request):
        silver_collection = Guitarra.objects.filter(color='Silver')[:3]
        strat_american_special = Guitarra.objects.filter(marca__nombre='Fender', sub_modelo__nombre='American Special')[0]
        fender_guitars = Guitarra.objects.filter(marca__nombre='Fender').exclude(sub_modelo__nombre='American Special').exclude(color='Silver')[:4]
        gibson_guitars = Guitarra.objects.filter(marca__nombre='Gibson')



        return render(request, "index.html", {'silver_collection': silver_collection, 'fender_guitars': fender_guitars, 'strat_american_special': strat_american_special, 'gibson_guitars': gibson_guitars})
