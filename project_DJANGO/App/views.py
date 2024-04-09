from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.shortcuts import render
from django.views.generic import View
from .models import Guitarra

# Create your views here.

class IndexView(View):
    def get(self, request):
        try:
            silver_collection = Guitarra.objects.filter(color='Silver')[:3]
            strat_american_special = self.get_american_special_guitar()
            fender_guitars = self.get_fender_guitars()
            gibson_guitars = self.get_gibson_guitars()
            
            return render(request, "index.html", {
                'silver_collection': silver_collection,
                'fender_guitars': fender_guitars,
                'strat_american_special': strat_american_special,
                'gibson_guitars': gibson_guitars
            })

        except Exception as e:
        
            print(f"Error en la vista IndexView: {e}")
            return render(request, "index.html")

    def get_american_special_guitar(self):
        return Guitarra.objects.filter(marca__nombre='Fender', sub_modelo__nombre='American Special').first()

    def get_fender_guitars(self):
        return Guitarra.objects.filter(marca__nombre='Fender').exclude(sub_modelo__nombre='American Special').exclude(color='Silver')[:4]

    def get_gibson_guitars(self):
        return Guitarra.objects.filter(marca__nombre='Gibson')
