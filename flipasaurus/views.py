from django.shortcuts import render, redirect
from flipasaurus.models import User, Card, Deck
from .forms import DeckForm, CardForm
from django.views.generic.edit import FormView


# Create your views here.

def test(request):
  return render(request, 'flipasaurus/base.html')

def create_deck(request):
  if request.method == 'POST':
    form = DeckForm(request.POST)
    if form.is_valid():
      deck = form.save()
      return redirect('/')
  else:
    form = DeckForm()
  return render(request, 'create_deck.html', {
    'form': form
  })


