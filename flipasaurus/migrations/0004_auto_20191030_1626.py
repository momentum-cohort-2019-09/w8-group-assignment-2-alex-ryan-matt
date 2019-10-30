# Generated by Django 2.2.6 on 2019-10-30 16:26

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flipasaurus', '0003_deck_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='update_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='deck',
            name='owner',
            field=models.ForeignKey(on_delete='models.CASCADE', related_name='decks', to=settings.AUTH_USER_MODEL),
        ),
    ]