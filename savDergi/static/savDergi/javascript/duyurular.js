const duyurularDivs = document.querySelectorAll('.duyurular_div');

duyurularDivs.forEach(div => {
    div.addEventListener('click', () => {
        div.querySelector('.duyurular_topic').click();
    });
});

const duyuruElements = document.querySelectorAll('.duyuru_element');

duyuruElements.forEach(element => {
    element.addEventListener('click', () => {
        element.querySelector('.duyuru_element-topic').click();
    });
});