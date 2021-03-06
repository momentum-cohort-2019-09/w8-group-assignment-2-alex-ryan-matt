from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.


class User(AbstractUser):
  
  def __str__(self):
    return self.username


class Card(models.Model):
  prompt = models.TextField()
  description = models.TextField()
  owner = models.ForeignKey(to=User, related_name='cards', on_delete=models.CASCADE, null=True, blank=True) #Make sure is read only .. FIX ME
  correct_flips = models.IntegerField(default=0)
  incorrect_flips = models.IntegerField(default=0)
  success_rate = models.DecimalField(default=None, max_digits=5, decimal_places=2, blank=True, null=True)
  deck = models.ForeignKey(to="Deck", related_name="cards", on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.prompt
    
  def get_success_rate(self):
    if self.incorrect_flips == 0:
      return 100
    else:
      return self.correct_flips/self.incorrect_flips

class Deck(models.Model):
  subject = models.CharField(max_length = 100, blank=True, null=True)
  title = models.CharField(max_length=100)
  owner = models.ForeignKey(to=User, related_name='decks', on_delete='models.CASCADE', null=True, blank=True)
  public = models.BooleanField(default=True) #HYPE
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title






