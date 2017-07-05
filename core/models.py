from django.db import models
from django.contrib.auth.models import User

class UserPreference(models.Model):
    PRICE_INTERVAL_CHOICES = (
        ('1', 'R$ 0,00 - R$ 40,00'),
        ('2', 'R$ 40,00 - R$ 80,00'),
        ('3', 'R$ 80,00 - R$ 120,00'),
        ('3', 'R$ 120,00 +')
    )

    date_created = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, related_name="preferences")
    platform = models.CharField(max_length=120, blank=True)
    price = models.CharField(max_length=1, choices=PRICE_INTERVAL_CHOICES, blank=True)
    genre = models.CharField(max_length=120, blank=True)


    def get_genres_list(self):
        return self.genre.split(',')


class UserHiddenPreference(models.Model):
    PRICE_INTERVAL_CHOICES = (
        ('1', 'R$ 0,00 - R$ 40,00'),
        ('2', 'R$ 40,00 - R$ 80,00'),
        ('3', 'R$ 80,00 - R$ 120,00'),
        ('3', 'R$ 120,00 +')
    )

    date_created = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, related_name="hidden_preferences")
    platform = models.CharField(max_length=120, blank=True)
    price = models.CharField(max_length=1, choices=PRICE_INTERVAL_CHOICES, blank=True)
    genre = models.CharField(max_length=120, blank=True)


    def get_genres_list(self):
        return self.genre.split(',')
# Create your models here.
