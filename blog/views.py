from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Card
# Create your views here.
def home(request):
    cards = Card.objects
    return render(request, 'home.html', {'cards' : cards})

def add(request):
    card = Card()
    card.title = request.POST['title']
    card.description = request.POST['description']
    card.writer = '정성훈'
    card.image = request.FILES['image']
    card.date = timezone.datetime.now()
    card.save()
    return redirect('/')