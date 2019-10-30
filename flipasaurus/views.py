from django.shortcuts import render, redirect, get_object_or_404
from flipasaurus.models import User, Card, Deck
from .forms import DeckForm, CardForm
from django.http import HttpResponse
from django.views.generic.edit import FormView
from rest_framework import viewsets
from flipasaurus.serializers import UserSerializer, CardSerializer, DeckSerializer
from rest_framework.decorators import action


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
  API endpoint that allows decks to be viewed or edited.
  """
  queryset = Deck.objects.all()
  serializer_class = DeckSerializer

def edit_card(request, pk):
  card = get_object_or_404(Card, pk=pk)

  if request == "POST":
    form = CardForm(instance=card, data = request.POST)
    if form.is_valid():
      form = form.save()
      return redirect(to='flipasaurus/edit_deck.html', pk=card.id) #Redirect to edit deck template
  else:
    form = CardForm(instance=card)

  return render(request, "flipasaurus/edit_card.html" , {
    "card": card,
    "form": form,
  })

