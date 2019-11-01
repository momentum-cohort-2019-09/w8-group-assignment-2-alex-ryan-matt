from flipasaurus.models import User, Card, Deck
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
  decks =  serializers.PrimaryKeyRelatedField(many=True, queryset=Deck.objects.all())
  class Meta:
    model = User
    fields = ['id','username','decks']

class CardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Card
    fields = ['prompt', 'description','owner','correct_flips','incorrect_flips','success_rate','deck', 'id']

class DeckSerializer(serializers.ModelSerializer):
  cards = CardSerializer(many=True)
  class Meta:
    model = Deck
    fields = ['subject','title','owner','cards','public','updated_at']

