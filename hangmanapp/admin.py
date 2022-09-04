from django.contrib import admin

from hangmanapp.models import GameWords, ListItem, Player

# Register your models here.
admin.site.register(ListItem)
admin.site.register(GameWords)
admin.site.register(Player)
