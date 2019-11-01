from django.shortcuts import render, redirect, get_object_or_404
from flipasaurus.models import User, Card, Deck
from .forms import DeckForm, CardForm
from django.http import HttpResponse
from django.views.generic.edit import FormView
from rest_framework import viewsets, permissions
from flipasaurus.serializers import UserSerializer, CardSerializer, DeckSerializer
from rest_framework.decorators import action
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from flipasaurus.permissions import IsOwnerOrReadOnly, IsUserOrReadOnly


# Create your views here.


def deck_test(request, pk):
  deck = DeckSerializer(Deck.objects.get(pk=pk))
  return render(request, 'flipasaurus/test_view.html', {'deck':deck})

@login_required(login_url='/accounts/login/')
def dashboard(request):
  return render(request, 'flipasaurus/dashboard.html')

@login_required(login_url='/accounts/login/')  
@csrf_exempt
def create_deck(request):
  if request.method == 'POST':
    form = DeckForm(request.POST)
    if form.is_valid():
      deck = form.save(commit=False)
      deck.owner = request.user
      deck.save()
      return redirect('view_deck', pk=deck.id)
  else:
    form = DeckForm()
  return render(request, 'flipasaurus/create_deck.html', {
    'form': form
  })

@login_required(login_url='/accounts/login')
@csrf_exempt
def artisanal_create_card(request, pk):
  deck = get_object_or_404(Deck, pk=pk)
  if request.method=='POST':
    response_data = {}
    form_data = json.loads(request.body)
    prompt = form_data['prompt']
    description = form_data['description']
    card = Card(prompt=prompt, description=description, owner=request.user, deck=deck)
    card.save()
    
    response_data['result'] = 'Success!'
    response_data['deckpk'] = deck.id
    response_data['prompt'] = card.prompt
    response_data['description'] = card.description
    response_data['owner'] = card.owner.username

    return HttpResponse(
      json.dumps(response_data),
      content_type="application/json"
    )
  else:
    return HttpResponse(
      json.dumps({'nothing to see':'this is not happening'}),
      content_type="application/json"
    )

  

@login_required(login_url='/accounts/login/')
@csrf_exempt
def view_deck(request, pk):
  deck = Deck.objects.get(id=pk)
  form = CardForm()
  return render(request, "flipasaurus/view_deck.html", {'deck': deck, 'form': form})

@login_required(login_url='/accounts/login/')
def delete_card(request, pk):
  Card.objects.get(id=pk).delete()
  return redirect(to='flipasaurus/edit_deck.html')

@login_required(login_url='/accounts/login/')
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
  return render(request, 'flipasaurus/edit_deck.html', {
    'deck': deck,
    'form': form
  })

@login_required(login_url='/accounts/login/')    
def delete_deck(request, pk):
  Deck.objects.get(id=pk).delete()
  return redirect(to='flipasaurus/dashboard.html')

class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

class CardViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows cards to be viewed or edited.
  """
  queryset = Card.objects.all()
  serializer_class = CardSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class DeckViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows decks to be viewed or edited.
  """
  queryset = Deck.objects.all()
  serializer_class = DeckSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def quiz(request, pk):
  deck = DeckSerializer(Deck.objects.get(pk=pk))
  return render(request, 'flipasaurus/quiz.html', {'deck': deck})

