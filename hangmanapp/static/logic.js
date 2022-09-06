function addItem() {
    console.log('add Item');
    let itemName = prompt('Neues Element hinzufügen');
    let formData = new FormData();
    let cookie = document.cookie;
    let cookieData = cookie.split('=');
    let methode = 'addItem';
    // let token = '{{ csrf_token }}';
    let token = cookieData[ 1 ];
    formData.append('methode', methode);
    formData.append('itemName', itemName);
    formData.append('csrfmiddlewaretoken', token);

    fetch('/hangman/', {
        method: 'POST',
        body: formData
    });
    window.location.reload();
}