

function checkLetter(event) {
    const wordLetters = JSON.parse(document.getElementById('wordLetters').textContent);
    console.log(wordLetters)
    const checkedLetters = JSON.parse(document.getElementById('checkedLetters').textContent);
    console.log(checkedLetters)
    const checkedLettersArray = checkedLetters.split(',')
    let formData = new FormData();
    let cookie = document.cookie;
    let cookieData = cookie.split('=');
    let token = cookieData[ 1 ];
    let letter = document.getElementById("letterInput").value.toUpperCase();
    let checktletter = false;

    checkedLettersArray.forEach(entry => {
        if (letter == entry && entry != '') {
            console.log('letter: ', letter);
            checktletter = true;
        }
    });


    if (letter !== '' && event.key === 'Enter') {
        if (checktletter) {
            console.log('this letter was alredy used!');
            document.getElementById('letterInput').value = '';
        }
        else {
            formData.append('letter', letter);
            formData.append('csrfmiddlewaretoken', token);
            fetch('/game/', {
                method: 'POST',
                body: formData
            });

            this.updateGame();
        }
    }
}

// document.getElementById('letterInput').addEventListener('keyup', function (event) {
//     console.log(event);
// });


function updateGame() {
    window.location.href = "//localhost:8000/updateGame/";
    window.location.reload();
}