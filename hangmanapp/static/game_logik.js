function checkLetter(event) {
    const wordLetters = JSON.parse(document.getElementById('wordLetters').textContent);
    // console.log(wordLetters)
    const checkedLetters = JSON.parse(document.getElementById('checkedLetters').textContent);
    // console.log(checkedLetters)
    let formData = new FormData();
    let cookie = document.cookie;
    let cookieData = cookie.split('=');
    let token = cookieData[ 1 ];
    let letter = document.getElementById("letterInput").value.toUpperCase();
    let checktletter = false;

    // prüft ob der Buchstabe bereits getippt wurde
    checkedLetters.forEach(entry => {
        if (letter == entry && entry != '') {
            checktletter = true;
        }
    });

    // Wenn der Input nicht leer ist und ein Enter Event getriggert wurde 
    // wird geprüft ob der Buchstabe bereits schonmal eingetippt wurde
    // und falls nicht wird eine Request ans Back End gestartet
    if (letter !== '' && event.key === 'Enter') {
        // das ß wird zu ss gemacht, deshalb braucht man für 
        // diesen Fall eine extra Abfrage
        if (letter.length == 2) {
            alert("ungültige Eingabe!");
            document.getElementById("letterInput").value = '';
        } else {
            // es sollen nur Buchstaben von A bis Z zugelassen
            if (letter.charCodeAt(0) < 65 || letter.charCodeAt(0) > 90) {
                alert("ungültige Eingabe!");
                document.getElementById("letterInput").value = '';
            } else {
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
    }
}

// document.getElementById('letterInput').addEventListener('keyup', function (event) {
//     console.log(event);
// });


function updateGame() {
    window.location.href = "//localhost:8000/updateGame/";
    window.location.reload();
}