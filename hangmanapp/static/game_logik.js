

function checkLetter(event) {
    let formData = new FormData();
    let cookie = document.cookie;
    let cookieData = cookie.split('=');
    let token = cookieData[ 1 ];
    let letter = document.getElementById("letterInput").value;
    let methode = 'check';

    if (letter !== '' && event.key === 'Enter') {
        console.log('Check Letter ' + letter);
        formData.append('methode', methode);
        formData.append('letter', letter);
        formData.append('csrfmiddlewaretoken', token);

        fetch('/game/', {
            method: 'POST',
            body: formData
        });
    }
}

// document.getElementById('letterInput').addEventListener('keyup', function (event) {
//     console.log(event);
// });