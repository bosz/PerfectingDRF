from django.db import models
from datetime import datetime

# Create your models here.
# Country
class Country(models.Model):
    name = models.TextField(max_length=100)
    code = models.TextField(max_length=100)

    def __str__(self):
        return self.name

# Club
class Club(models.Model):
    name = models.TextField(max_length=100)
    country = models.ForeignKey(Country, related_name='clubs_country', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Membership
class Membership(models.Model):
    club = models.ForeignKey(Club, related_name="club_membership", default=None, on_delete=models.CASCADE)
    # player = models.ForeignKey(Player, related_name="player_membership", default=None, on_delete=models.CASCADE)
    signed_on = models.DateField(default=datetime.now)
    contract_img = models.FileField()

    def __str__(self):
        return "Sign for "+str(self.club)+" on "+str(self.signed_on)

# Player
class Player(models.Model):
    name = models.TextField(max_length=100)
    age = models.IntegerField()
    country = models.ForeignKey(Country, related_name='players_country', on_delete=models.CASCADE)
    membership = models.ManyToManyField(Membership, blank=True)

    def __str__(self):
        return self.name


