from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm, ListingForm
from django.core.mail import send_mail

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
def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return HttpResponseRedirect(reverse('band-detail', kwargs={'band_id': band.id}))
    else:
        form = BandForm()
    return render(request, 
        'listings/band_create.html',
        {'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return HttpResponseRedirect(reverse('band-detail', kwargs={'id': band.id}))
    else:
        form = BandForm(instance=band)
    return render(request,
                'listings/band_update.html',
                {'form': form})

def about(request):
    return render(request,
        'listings/about.html')

def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()
    return render(request,
        'listings/contact.html',
        {'form': form})
# def contact(request):
#     return render(request,
#                  'listings/contact.html')
def email_sent(request):
    return render(request,
        'listings/email_sent.html')

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

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            listing = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return HttpResponseRedirect(reverse('listing-detail', kwargs={'listing_id': listing.id}))
    else:
        form = ListingForm()
    return render(request, 
        'listings/listing_create.html',
        {'form': form})