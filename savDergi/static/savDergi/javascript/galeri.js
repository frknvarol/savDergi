const albumDiv = document.querySelectorAll('.album_div');

albumDiv.forEach(div => {
    div.addEventListener('click', () => {
        div.querySelector('.album_name a').click();
    })
});