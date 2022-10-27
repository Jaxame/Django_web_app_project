from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def band_list(request):  # renommer la fonction de vue
   bands = Band.objects.all()
   return render(request,
           'listings/band_list.html',  # pointe vers le nouveau nom de modèle
           {'bands': bands})

def about(request):
    return render(request,
                 'listings/about.html')

def contact(request):
    return render(request,
                 'listings/contact.html')

def listings(request):
    listings = Listing.objects.all()
    return render(request,
                 'listings/listing.html',
                 {'listings': listings})
