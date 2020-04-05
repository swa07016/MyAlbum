from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Card
# Create your views here.
def home(request):
    cards = Card.objects.order_by('-date')
    return render(request, 'home.html', {'cards' : cards})

def add(request):
    card = Card()
    card.title = request.POST['title']
    card.description = request.POST['description']
    card.writer = request.user.get_username()
    card.image = request.FILES['image']
    card.date = timezone.datetime.now()
    card.save()
    return redirect('/')

def delete(request):
    #print(request.POST['cardid'])
    card = Card.objects.get(id=request.POST['cardid'])
    card.delete()
    return redirect('/')