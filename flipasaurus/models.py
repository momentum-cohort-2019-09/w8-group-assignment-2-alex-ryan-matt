from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
  pass


class Card(models.Model):
  prompt = models.TextField()
  description = models.TextField()
  owner = models.ForeignKey(to="User", related_name="card", on_delete="models.CASCADE", ) #Make sure is read only .. FIX ME
  correct_flips = models.IntegerField(default=0)
  incorrect_flips = models.IntegerField(default=0)
  success_rate = models.DecimalField(default=None, max_digits=5, decimal_places=2, blank=True, null=True)


class Deck(models.Model):
  subject = models.CharField(max_length = 100, blank=True, null=True)
  title = models.CharField(max_length=100)
  owner = models.ForeignKey(to="User", related_name="deck", on_delete="models.CASCADE",)
  cards = models.ManyToManyField(to="Card", related_name="cards",)
  public = models.BooleanField(default=True) #HYPE






