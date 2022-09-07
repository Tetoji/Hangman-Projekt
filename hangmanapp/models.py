from datetime import date
from django.db import models

class ListItem(models.Model): 
    createted_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' ' + self.name


# Model für die Spiel Wörter
class GameWords(models.Model): 
    word = models.CharField(max_length=200)
    difficulty = models.SmallIntegerField(default=1)

    def __str__(self):
        return str(self.id) + ' ' + self.word


# Model für die Spieler
class Player(models.Model): 
    name = models.CharField(max_length=200)
    wins = models.SmallIntegerField(default=0)
    loses = models.SmallIntegerField(default=0)

    def __str__(self):
        return str(self.id) + ' ' + self.name


# Model für das aktive Wort
class AktivWord(models.Model): 
    word = models.CharField(max_length=200)
    hitLocations = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.id) + ' ' + self.word

# Model zur Prüfung der Eingaben
class CheckLetters(models.Model): 
    checkedLetters = models.CharField(max_length=500)
    fails = models.SmallIntegerField(default=0)
    hits = models.SmallIntegerField(default=0)
    
    def __str__(self):
        return str(self.id) + ' ' + self.checkedLetters

# Model für die Spielzeit
class GameTime(models.Model): 
    timeStamp = models.CharField(max_length=500)
    
    def __str__(self):
        return str(self.id) + ' ' + self.timeStamp

# Tipp
class Tipp(models.Model): 
    used = models.CharField(max_length=500)
    
    def __str__(self):
        return str(self.id) + ' ' + self.used