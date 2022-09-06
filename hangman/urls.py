"""hangman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

<<<<<<< HEAD
from hangmanapp.views import game, hangman, loseGame, menue, updateGame, winGame
=======
from hangmanapp.views import game, hangman, menue, updateGame
>>>>>>> cef74e3b673ff16c671ee91fbe73601c5f7a5614

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hangman/', hangman),
    path('menue/', menue),
    path('game/', game),
    path('updateGame/', updateGame),
<<<<<<< HEAD
    path('winGame/', winGame),
    path('loseGame/', loseGame),
=======
>>>>>>> cef74e3b673ff16c671ee91fbe73601c5f7a5614
]

admin.site.index_title = "Hangman" 

admin.site.site_header = "Admin Portal"
admin.site.site_title = "Admin Portal"
