function selectWord() {
    let player = (document.getElementById('playerInput').value).toUpperCase();
    const allPlayer = JSON.parse(document.getElementById('allPlayer').textContent);
    console.log(allPlayer);
    console.log(player);
    let newPlayer = true;
    let formData = new FormData();
    let cookie = document.cookie;
    let cookieData = cookie.split('=');
    let token = cookieData[ 1 ];

    allPlayer.forEach(enttry => {
        if (enttry == player) {
            newPlayer = false;
        }
    });

    console.log(newPlayer);

    formData.append('player', player)
    formData.append('newPlayer', newPlayer);
    formData.append('csrfmiddlewaretoken', token);

    fetch('/menue/', {
        method: 'POST',
        body: formData
    });
    window.location.href = "//localhost:8000/game/";
}