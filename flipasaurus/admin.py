from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Card, Deck

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Card)
admin.site.register(Deck)

