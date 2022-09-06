function selectWord() {
<<<<<<< HEAD
    let player = (document.getElementById('playerInput').value).toUpperCase();
    const allPlayer = JSON.parse(document.getElementById('allPlayer').textContent);
    console.log(allPlayer);
    console.log(player);
    let newPlayer = true;
=======
    console.log('select Word');
>>>>>>> cef74e3b673ff16c671ee91fbe73601c5f7a5614
    let formData = new FormData();
    let cookie = document.cookie;
    let cookieData = cookie.split('=');
    let token = cookieData[ 1 ];
<<<<<<< HEAD

    allPlayer.forEach(enttry => {
        if (enttry == player) {
            newPlayer = false;
        }
    });

    console.log(newPlayer);

    formData.append('player', player)
    formData.append('newPlayer', newPlayer);
=======
>>>>>>> cef74e3b673ff16c671ee91fbe73601c5f7a5614
    formData.append('csrfmiddlewaretoken', token);

    fetch('/menue/', {
        method: 'POST',
        body: formData
    });
    window.location.href = "//localhost:8000/game/";
}