function checkLetter(event) {
    // const wordLetters = JSON.parse(document.getElementById('wordLetters').textContent);
    // console.log(wordLetters)
    const checkedLetters = JSON.parse(document.getElementById('checkedLetters').textContent);
    // console.log(checkedLetters)
    let formData = new FormData();
    let cookie = document.cookie;
    let cookieData = cookie.split('=');
    let token = cookieData[ 1 ];
    let letter = document.getElementById("letterInput").value.toUpperCase();
    let checktletter = false;
    let isTipp = 0;

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
            // alert("ungültige Eingabe!");
            this.startSnackBar();
            document.getElementById("letterInput").value = '';
        } else {
            // es sollen nur Buchstaben von A bis Z zugelassen
            if (letter.charCodeAt(0) < 65 || letter.charCodeAt(0) > 90) {
                // alert("ungültige Eingabe!");
                this.startSnackBar();
                document.getElementById("letterInput").value = '';
            } else {
                if (checktletter) {
                    console.log('this letter was alredy used!');
                    document.getElementById('letterInput').value = '';
                }
                else {
                    formData.append('letter', letter);
                    formData.append('isTipp', isTipp);
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

function tipp() {
    let tipp = prompt('Tipp eingeben').toUpperCase();
    const checkedLetters = JSON.parse(document.getElementById('checkedLetters').textContent);
    let formData = new FormData();
    let cookie = document.cookie;
    let cookieData = cookie.split('=');
    let token = cookieData[ 1 ];
    let checktletter = false;
    let isTipp = 1;

    // prüft ob der Buchstabe bereits getippt wurde
    checkedLetters.forEach(entry => {
        if (tipp == entry && entry != '') {
            checktletter = true;
        }
    });

    // das ß wird zu ss gemacht, deshalb braucht man für 
    // diesen Fall eine extra Abfrage
    if (tipp.length == 2) {
        // alert("ungültige Eingabe!");
        this.startSnackBar();
    } else {
        // es sollen nur Buchstaben von A bis Z zugelassen
        if (tipp.charCodeAt(0) < 65 || tipp.charCodeAt(0) > 90) {
            this.startSnackBar();
        } else {
            if (checktletter) {
                console.log('this letter was alredy used!');
                document.getElementById('letterInput').value = '';
            }
            else {
                formData.append('letter', tipp);
                formData.append('csrfmiddlewaretoken', token);
                formData.append('isTipp', isTipp);

                fetch('/game/', {
                    method: 'POST',
                    body: formData
                });

                this.updateGame();
            }
        }
    }
}

// document.getElementById('letterInput').addEventListener('keyup', function (event) {
//     console.log(event);
// });

function startSnackBar() {
    console.log('Snack');
    var x = document.getElementById("snackbar");
    x.className = "show";
    setTimeout(function () { x.className = x.className.replace("show", ""); }, 3000);
}

function updateGame() {
    window.location.href = "//localhost:8000/updateGame/";
    window.location.reload();
}