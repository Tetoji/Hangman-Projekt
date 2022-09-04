from django.shortcuts import render

from hangmanapp.models import GameWords, ListItem

# Zum Rendern der HTML Dateien
def hangman(request):
    if request.method == 'POST':
        if request.POST['methode'] != 'check':
            print('Recived data:', request.POST['itemName'])
            ListItem.objects.create(name = request.POST['itemName'])
        else: 
            print('check Methode')
    # ListItem.objects.get(id=1)
    # ListItem.objects.filter(name='test')
    all_items = ListItem.objects.all()
    return render(request, 'hangman_oberflaeche.html', {'all_items': all_items})


def menue(request):
    return render(request, 'menue.html')

def game(request):
    if request.method == 'POST':
        print('Recived data:', request.POST['letter'])
        print('searchWord:')

    # holt zufälliges Wort aus der Datenbanktabelle
    searchWord = GameWords.objects.order_by('?').first()
    # neue Datenbanktabelle erstellen und das searchword hier überschreiben
    wordLetters = []
    iterator = 0

    for letter in searchWord.word:
        wordLetters.append(iterator)
        iterator = iterator + 1

    return render(request, 'hangman_game.html', {'wordLetters': wordLetters})

