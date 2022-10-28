from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from listings.models import Band, Listing
from listings.forms import ContactUsForm

def band_list(request):  
   bands = Band.objects.all()
   return render(request,
           'listings/band_list.html',  
           {'bands': bands})

def band_detail(request, band_id):
    band = get_object_or_404(Band, id=band_id)
#   band = Band.objects.get(id=band_id)  
    return render(request,
          'listings/band_detail.html',
          {'band': band}) 

# def band_detail(request, band_id):  
#    return render(request,
#           'listings/band_detail.html',
#          {'id': band_id}) 

def about(request):
    return render(request,
                 'listings/about.html')

def contact(request):
    form = ContactUsForm()  
    return render(request,
        'listings/contact.html',
        {'form': form})
# def contact(request):
#     return render(request,
#                  'listings/contact.html')

def listing_list(request):
    listings = Listing.objects.all()
    return render(request,
                 'listings/listing_list.html',
                 {'listings': listings})

def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
# band = Band.objects.get(id=band_id)  
    return render(request,
          'listings/listing_detail.html',
          {'listing': listing}) 