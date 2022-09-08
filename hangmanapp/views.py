from datetime import datetime
from time import time
from django.shortcuts import render, redirect,  get_object_or_404

from hangmanapp.models import AktivWord, CheckLetters, GameTime, GameWords, ListItem, Player, Tipp
#from hangmanapp.static.myClasses import LetterLocationClass

class LetterLocationClass:
    # Klasse für die 
    def __init__(self, letter, location):
        self.letter = letter
        self.location = location
        

# Zum Rendern der HTML Dateien
def hangman(request):
    if request.method == 'POST':
        #if request.POST['methode'] != 'check':
        print('Recived data:', request.POST['itemName'])
        ListItem.objects.create(name = request.POST['itemName'])
        #else: 
        #    print('check Methode')
    # ListItem.objects.get(id=1)
    # ListItem.objects.filter(name='test')
    all_items = ListItem.objects.all()
    return render(request, 'hangman_oberflaeche.html', {'all_items': all_items})

def index(request):
    return redirect(menue)

def menue(request):
    # bei Post request wird der folgende Code ausgeführt
    if request.method == 'POST':
        # holt Spieler Namen und flag ob neuer Spieler
        player = request.POST['player']
        newPlayer = request.POST['newPlayer']
        # falls neuer Spieler erstelle neuen Datenbankeintrag für Spieler
        if newPlayer != 'false':
            Player.objects.create(name = player)
        # holt zufälliges Wort aus der Datenbanktabelle
        searchWord = GameWords.objects.order_by('?').first()
        # das Wort in einer anderen Datenbanktabelle speichern
        # in dieser Tabelle soll nur der erste Eintrag verarbeitet werden
        # Wenn kein Eintag gefunden wird ein 404 Error zurückgegben
        selectedWord = get_object_or_404(AktivWord, pk=1)
        checkedLetters = get_object_or_404(CheckLetters, pk=1)
        dataTime = get_object_or_404(GameTime, pk=1)
        tipp = get_object_or_404(Tipp, pk=1)
        selectedWord.word = searchWord.word.upper()
        selectedWord.hitLocations = ''
        checkedLetters.checkedLetters = ''
        tipp.used = ''
        tipp.save()
        checkedLetters.fails = 0
        checkedLetters.hits = 0
        selectedWord.save()
        checkedLetters.save()
        timeStamp = time()
        timeDate = datetime.fromtimestamp(timeStamp)
        dataTime.timeStamp = timeDate.strftime("%H:%M:%S")
        dataTime.save()
    
    allPlayer = Player.objects.all()
    playerArray = []

    for player in allPlayer:
        playerArray.append(player.name)

    # liefert die menue HTML Seite zurück
    return render(request, 'menue.html', {'allPlayer': playerArray})


def game(request):
    if request.method == 'POST':
        # holt den Wert der beim Request mitgegeben wird
        checkLetter = request.POST['letter']
        isTipp = request.POST['isTipp']
        print('isTipp: ', isTipp)
        # holt das zuvor selektierte Wort aus der Datenbanktabelle
        aktivWord = get_object_or_404(AktivWord, pk=1)
        checkedLetters = get_object_or_404(CheckLetters, pk=1)
        tipp = get_object_or_404(Tipp, pk=1)
        hitLocations = ''
        previousLocations = ''
        letterIterator = 0
        hit = 0

        #hängt eingegebenen Buchstaben an String dran und speichert den String dann in der Datenbank  
        if checkedLetters.checkedLetters != '':
            checkedLetters.checkedLetters = checkedLetters.checkedLetters + ',' + checkLetter
        else:
            checkedLetters.checkedLetters =  checkLetter
        checkedLetters.save()

        # überprüft ob es schon Treffer Stellen gibt falls ja werden sie in einer Variable zwischen gespeichert
        if aktivWord.hitLocations != '':
            previousLocations = aktivWord.hitLocations

        # vergleicht jeden Buchstaben im Wort mit dem gesuchten und 
        # speichert beim Treffer die Stelle des Buchstaben im String
        # bei mehreren Treffern werden die Stellen mit einem Komma gtrennt 
        for letter in aktivWord.word:
            if letter == checkLetter:
                #markiert den Treffer
                hit = hit + 1
                if hitLocations == '':
                    hitLocations = str(letterIterator) + '=' + checkLetter
                else:
                    hitLocations = hitLocations + ',' + str(letterIterator) + '=' + checkLetter
            letterIterator = letterIterator + 1
        # überschreibt die hitlocations im Datenbankeintrag
        if hitLocations != '':
            aktivWord.hitLocations = hitLocations + ',' + previousLocations
            aktivWord.save()

        if isTipp == '0':
            # falls es keinen Treffer gab wird der FailCounter um 1 erhöht 
            if hit == 0:
                checkedLetters.fails = checkedLetters.fails + 1
                checkedLetters.save()
        else: 
            tipp.used = 'true'
            tipp.save()

        if hit != 0:
            checkedLetters.hits = checkedLetters.hits + hit
            checkedLetters.save()
         

    # holt das zuvor selektierte Wort aus der Datenbanktabelle
    searchWord = AktivWord.objects.get(id=1)
    checkedLetters = get_object_or_404(CheckLetters, pk=1)
    tipp = get_object_or_404(Tipp, pk=1)
    wordLetters = getLetterArray(searchWord)
    checkedLettersArray = getcheckedLettersArry(checkedLetters)
    trys = len(checkedLettersArray)
    fails = checkedLetters.fails

    if checkWin(searchWord):
        getGameTime()
        return redirect('http://localhost:8000/winGame/')
    elif checkedLetters.fails >= 6:
        getGameTime()
        return redirect('http://localhost:8000/loseGame/')
    else:
        # liefert die hangman_game HTML Seite zurück und übergibt an diese das Buchstaben Array
        return render(request, 'hangman_game.html', {'wordLetters': wordLetters, 'checkedLetters': checkedLettersArray, 'trys': trys, 'hits': checkedLetters.hits, 'fails': fails, 'tipp': tipp.used})

def getGameTime():
    startTime = get_object_or_404(GameTime, pk=1)
    endStamp = time()
    endDate = datetime.fromtimestamp(endStamp)
    endTime = endDate.strftime("%H:%M:%S")
    startArray = str(startTime.timeStamp).split(':')
    endArray = endTime.split(':')
    startsecends = float(startArray[0]) * 360 + float(startArray[1]) * 60 + float(startArray[2])
    endsecends = float(endArray[0]) * 360 + float(endArray[1]) * 60 + float(endArray[2])
    gameTime = endsecends - startsecends

    return gameTime 


def updateGame(request):
    # holt das aktive Wort aus der Datenbanktabelle
    aktivWord = get_object_or_404(AktivWord, pk=1)
    checkedLetters = get_object_or_404(CheckLetters, pk=1)
    tipp = get_object_or_404(Tipp, pk=1)
    wordLetters = getLetterArray(aktivWord)
    checkedLettersArray = getcheckedLettersArry(checkedLetters)
    trys = len(checkedLettersArray)
    fails = checkedLetters.fails

    return render(request, 'hangman_game.html', {'wordLetters': wordLetters, 'checkedLetters': checkedLettersArray, 'trys': trys, 'hits': checkedLetters.hits, 'fails': fails, 'tipp': tipp.used})

def winGame(request):
    aktivWord = get_object_or_404(AktivWord, pk=1)
    checkedLetters = get_object_or_404(CheckLetters, pk=1)
    aktivWord.hitLocations = ''
    aktivWord.save()
    checkedLetters.checkedLetters = ''
    checkedLetters.fails = 0
    checkedLetters.save()
    gameTime = getGameTime()

    return render(request, 'winpage.html', {'gameTime': gameTime})


def loseGame(request):
    aktivWord = get_object_or_404(AktivWord, pk=1)
    checkedLetters = get_object_or_404(CheckLetters, pk=1)
    aktivWord.hitLocations = ''
    aktivWord.save()
    checkedLetters.checkedLetters = ''
    checkedLetters.fails = 0
    checkedLetters.save()
    gameTime = getGameTime()

    return render(request, 'losepage.html', {'gameTime': gameTime})


def getcheckedLettersArry(checkedLetters):
    lettersArray = []

    for letter in checkedLetters.checkedLetters:
        if letter != ',':
            lettersArray.append(letter)

    return sorted(lettersArray) 


# liefert das Buchstaben Array
def getLetterArray(aktivWord):
    letterLocations = [] 
    wordLetters = []
    iterator = 0
    marker = 1
    letter = ''
    location = '' 
    # falls Buchstaben bereits gefunden wurden müssen diese aus dem 
    # string zum Object verarbeitet werden
    if aktivWord.hitLocations != '':
        for character in aktivWord.hitLocations:
            if character != '=' and character != ',' and marker == 1:
                location = location + character
            elif character == '=':
                marker = 2
            elif character != ',' and marker == 2:
                letter = character
                letterLocation = LetterLocationClass(letter, location)
                location = '' 
                letterLocations.append(letterLocation)
                marker = 1
    # falls das Array Objecte beinhaltet werden aus dem den Objecten die 
    # genauen Positionen der Buchstaben bestimmt und im Buchstaben Array positioniert
    if len(letterLocations) != 0:
        marker = 0
        for letter in aktivWord.word:
            for letterLocation in letterLocations:
                if letterLocation.location == str(iterator):
                    wordLetters.append(letterLocation.letter)
                    marker = 1
            if marker == 0:
                wordLetters.append('')
            marker = 0
            iterator = iterator + 1

    else:        
        # zählt die Buchstaben im Wort und speichert diese im Array
        for letter in aktivWord.word:
            wordLetters.append('')
            iterator = iterator + 1

    return wordLetters


def checkWin(aktivWord):
    isWin = False
    marker = 0
    for charackter in aktivWord.hitLocations:
        if charackter == '=':
            marker = marker + 1
    if marker == len(aktivWord.word):
        isWin = True

    return isWin
