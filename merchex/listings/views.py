from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def band_list(request):  
   bands = Band.objects.all()
   return render(request,
           'listings/band_list.html',  
           {'bands': bands})

def band_detail(request, band_id):  
   return render(request,
          'listings/band_detail.html',
         {'id': band_id}) 

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
