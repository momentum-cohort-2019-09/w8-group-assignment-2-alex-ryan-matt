# Generated by Django 2.2.6 on 2019-10-29 22:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipasaurus', '0003_deck_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='owner',
            field=models.ForeignKey(on_delete='models.CASCADE', related_name='decks', to=settings.AUTH_USER_MODEL),
        ),
    ]
