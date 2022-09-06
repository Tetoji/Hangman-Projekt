<<<<<<< HEAD
from django.shortcuts import render, redirect,  get_object_or_404

from hangmanapp.models import AktivWord, CheckLetters, GameWords, ListItem, Player
=======
from django.shortcuts import render, get_object_or_404

from hangmanapp.models import AktivWord, CheckLetters, GameWords, ListItem
>>>>>>> cef74e3b673ff16c671ee91fbe73601c5f7a5614
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


def menue(request):
    # bei Post request wird der folgende Code ausgeführt
    if request.method == 'POST':
<<<<<<< HEAD
        # holt Spieler Namen und flag ob neuer Spieler
        player = request.POST['player']
        newPlayer = request.POST['newPlayer']
        print('newPlayer ', newPlayer)
        # falls neuer Spieler erstelle neuen Datenbankeintrag für Spieler
        if newPlayer != 'false':
            Player.objects.create(name = player)
=======
>>>>>>> cef74e3b673ff16c671ee91fbe73601c5f7a5614
        # holt zufälliges Wort aus der Datenbanktabelle
        searchWord = GameWords.objects.order_by('?').first()
        # das Wort in einer anderen Datenbanktabelle speichern
        # in dieser Tabelle soll nur der erste Eintrag verarbeitet werden
        # Wenn kein Eintag gefunden wird ein 404 Error zurückgegben
        selectedWord = get_object_or_404(AktivWord, pk=1)
        checkedLetters = get_object_or_404(CheckLetters, pk=1)
        selectedWord.word = searchWord.word.upper()
        selectedWord.hitLocations = ''
        checkedLetters.checkedLetters = ''
        selectedWord.save()
        checkedLetters.save()
<<<<<<< HEAD
    
    allPlayer = Player.objects.all()
    playerArray = []

    for player in allPlayer:
        playerArray.append(player.name)

    # liefert die menue HTML Seite zurück
    return render(request, 'menue.html', {'allPlayer': playerArray})

=======
    # liefert die menue HTML Seite zurück
    return render(request, 'menue.html')
>>>>>>> cef74e3b673ff16c671ee91fbe73601c5f7a5614


def game(request):
    if request.method == 'POST':
        # holt den Wert der beim Request mitgegeben wird
        checkLetter = request.POST['letter']
        # holt das zuvor selektierte Wort aus der Datenbanktabelle
        aktivWord = get_object_or_404(AktivWord, pk=1)
        checkedLetters = get_object_or_404(CheckLetters, pk=1)
        hitLocations = ''
        previousLocations = ''
        letterIterator = 0
<<<<<<< HEAD
        hit = False

        #hängt eingegebenen Buchstaben an String dran und speichert den String dann in der Datenbank  
=======

>>>>>>> cef74e3b673ff16c671ee91fbe73601c5f7a5614
        if checkedLetters.checkedLetters != '':
            checkedLetters.checkedLetters = checkedLetters.checkedLetters + ',' + checkLetter
        else:
            checkedLetters.checkedLetters =  checkLetter
        checkedLetters.save()

<<<<<<< HEAD
        # überprüft ob es schon Treffer Stellen gibt falls ja werden sie in einer Variable zwischen gespeichert
=======
>>>>>>> cef74e3b673ff16c671ee91fbe73601c5f7a5614
        if aktivWord.hitLocations != '':
            previousLocations = aktivWord.hitLocations

        # vergleicht jeden Buchstaben im Wort mit dem gesuchten und 
        # speichert beim Treffer die Stelle des Buchstaben im String
        # bei mehreren Treffern werden die Stellen mit einem Komma gtrennt 
        for letter in aktivWord.word:
            if letter == checkLetter:
<<<<<<< HEAD
                #markiert den Treffer
                hit = True
=======
>>>>>>> cef74e3b673ff16c671ee91fbe73601c5f7a5614
                if hitLocations == '':
                    hitLocations = str(letterIterator) + '=' + checkLetter
                else:
                    hitLocations = hitLocations + ',' + str(letterIterator) + '=' + checkLetter
            letterIterator = letterIterator + 1
        # überschreibt die hitlocations im Datenbankeintrag
        if hitLocations != '':
            aktivWord.hitLocations = hitLocations + ',' + previousLocations
            aktivWord.save()
<<<<<<< HEAD

        # falls es keinen Treffer gab wird der FailCounter um 1 erhöht 
        if (not hit): 
            checkedLetters.fails = checkedLetters.fails + 1
            checkedLetters.save()
=======
>>>>>>> cef74e3b673ff16c671ee91fbe73601c5f7a5614
         

    # holt das zuvor selektierte Wort aus der Datenbanktabelle
    searchWord = AktivWord.objects.get(id=1)
<<<<<<< HEAD
    checkedLetters = get_object_or_404(CheckLetters, pk=1)
    wordLetters = getLetterArray(searchWord)

    if checkWin(searchWord):
        return redirect('http://localhost:8000/winGame/')
    elif checkedLetters.fails >= 6:
        return redirect('http://localhost:8000/loseGame/')
    else:
        # liefert die hangman_game HTML Seite zurück und übergibt an diese das Buchstaben Array
        return render(request, 'hangman_game.html', {'wordLetters': wordLetters, 'hitlocations': searchWord.hitLocations, 'checkedLetters': checkedLetters.checkedLetters})


def updateGame(request):
    # holt das aktive Wort aus der Datenbanktabelle
    aktivWord = get_object_or_404(AktivWord, pk=1)
    checkedLetters = get_object_or_404(CheckLetters, pk=1)
    wordLetters = getLetterArray(aktivWord)
    return render(request, 'hangman_game.html', {'wordLetters': wordLetters, 'hitlocations': aktivWord.hitLocations, 'checkedLetters': checkedLetters.checkedLetters})

def winGame(request):
    aktivWord = get_object_or_404(AktivWord, pk=1)
    checkedLetters = get_object_or_404(CheckLetters, pk=1)
    aktivWord.hitLocations = ''
    aktivWord.save()
    checkedLetters.checkedLetters = ''
    checkedLetters.fails = 0
    checkedLetters.save()

    return render(request, 'winpage.html')


def loseGame(request):
    aktivWord = get_object_or_404(AktivWord, pk=1)
    checkedLetters = get_object_or_404(CheckLetters, pk=1)
    aktivWord.hitLocations = ''
    aktivWord.save()
    checkedLetters.checkedLetters = ''
    checkedLetters.fails = 0
    checkedLetters.save()

    return render(request, 'losepage.html')



=======
    wordLetters = getLetterArray(searchWord)
    # liefert die hangman_game HTML Seite zurück und übergibt an diese das Buchstaben Array
    return render(request, 'hangman_game.html', {'wordLetters': wordLetters, 'hitlocations': searchWord.hitLocations})


def updateGame(request):
    # holt das aktive Wort aus der Datenbanktabelle
    aktivWord = get_object_or_404(AktivWord, pk=1)
    checkedLetters = get_object_or_404(CheckLetters, pk=1)
    wordLetters = getLetterArray(aktivWord)
    return render(request, 'hangman_game.html', {'wordLetters': wordLetters, 'hitlocations': aktivWord.hitLocations, 'checkedLetters': checkedLetters.checkedLetters})



>>>>>>> cef74e3b673ff16c671ee91fbe73601c5f7a5614
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
                wordLetters.append('0')
            marker = 0
            iterator = iterator + 1
<<<<<<< HEAD

    else:        
        # zählt die Buchstaben im Wort und speichert diese im Array
        for letter in aktivWord.word:
            wordLetters.append('0')
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
=======

    else:        
        # zählt die Buchstaben im Wort und speichert diese im Array
        for letter in aktivWord.word:
            wordLetters.append('0')
            iterator = iterator + 1

    return wordLetters
>>>>>>> cef74e3b673ff16c671ee91fbe73601c5f7a5614

