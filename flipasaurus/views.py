from django.shortcuts import render, redirect, get_object_or_404
from flipasaurus.models import User, Card, Deck
from .forms import DeckForm, CardForm
from django.http import HttpResponse
from django.views.generic.edit import FormView
from rest_framework import viewsets
from flipasaurus.serializers import UserSerializer, CardSerializer, DeckSerializer

# Create your views here.

def test(request):
  return render(request, 'base.html')

def dashboard(request):
  return render(request, 'flipasaurus/dashboard.html')
  
def create_deck(request):
  if request.method == 'POST':
    form = DeckForm(request.POST)
    if form.is_valid():
      deck = form.save()
      return redirect(to=deck)
  else:
    form = DeckForm()
  return render(request, 'create_deck.html', {
    'form': form
  })

def create_card(request):
  if request.method == 'POST':
    form = CardForm(request.POST)
    if form.is_valid():
      card = form.save()
      return redirect(to=card)
  else:
    form = CardForm()
  return render(request, 'create_card.html', {
    'form': form
  })

def delete_card(request, pk):
  Card.objects.get(id=pk).delete()
  return redirect('/')

def edit_deck(request, pk):
  deck = get_object_or_404(Deck, id=pk)
  if request.method == 'POST':
    form = DeckForm(request.POST, instance=deck)
    if form.is_valid():
      deck = form.save(commit=False)
      deck.save()
      return redirect('/')
  else:
    form = DeckForm()
  return render(request, 'edit_deck.html', {
    'form': form
  })
    
def delete_deck(request, pk):
  Deck.objects.get(id=pk).delete()
  return redirect('/')

class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = User.objects.all()
  serializer_class = UserSerializer

class CardViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows cards to be viewed or edited.
  """
  queryset = Card.objects.all()
  serializer_class = CardSerializer

class DeckViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows cards to be viewed or edited.
  """
  queryset = Deck.objects.all()
  serializer_class = DeckSerializer
