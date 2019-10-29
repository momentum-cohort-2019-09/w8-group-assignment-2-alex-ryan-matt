from django import forms
from .models import Deck, Card


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['title', 'subject', 'public']


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['prompt', 'description']

