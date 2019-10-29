from django.shortcuts import render
from flipasaurus.models import User, Card, Deck
from rest_framework import viewsets
from flipasaurus.serializers import UserSerializer, CardSerializer, DeckSerializer

# Create your views here.

def test(request):
  return render(request, 'base.html')

def dashboard(request):
  return render(request, 'flipasaurus/dashboard.html')

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
