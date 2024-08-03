const duyurularDiv = document.querySelectorAll('.duyurular_div')

duyurularDiv.forEach(div => {
    div.addEventListener('click', () => {
        div.querySelector('.duyurular_topic').click();
    });
});