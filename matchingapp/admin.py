from django.contrib import admin
from .models import Country, Player, Club, Membership

admin.site.register(Country)
admin.site.register(Player)
admin.site.register(Club)
admin.site.register(Membership)
# Register your models here.
