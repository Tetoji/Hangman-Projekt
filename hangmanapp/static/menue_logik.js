function selectWord() {
    console.log('select Word');
    let formData = new FormData();
    let cookie = document.cookie;
    let cookieData = cookie.split('=');
    let token = cookieData[ 1 ];
    formData.append('csrfmiddlewaretoken', token);

    fetch('/menue/', {
        method: 'POST',
        body: formData
    });
    window.location.href = "//localhost:8000/game/";
}