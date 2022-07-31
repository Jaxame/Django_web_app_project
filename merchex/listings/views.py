from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
    """)

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def contact(request):
    return HttpResponse('<h1>Contact us !</h1> <p>Adresse</p>')

def listings(request):
    listings = Listing.objects.all()
    return HttpResponse(f"""
        <h1>Listings !</h1>
        <p>Titre des affiches :<p>
        <ul>
            <li>{listings[0].name}</li>
            <li>{listings[1].name}</li>
            <li>{listings[2].name}</li>
            <li>{listings[3].name}</li>
        </ul>
    """)