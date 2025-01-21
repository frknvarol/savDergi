const duyurularDivs = document.querySelectorAll('.duyuru-sayi_element');

duyurularDivs.forEach(div => {
    div.addEventListener('click', () => {
        div.querySelector('a').click();
    });
});



const duyuruElements = document.querySelectorAll('.duyuru_element');

duyuruElements.forEach(element => {
    element.addEventListener('click', () => {
        element.querySelector('.duyuru_element-topic').click();
    });
});


const duyuruContainers = document.querySelectorAll('.duyuru-sayi_container')



if (duyuruContainers[0].offsetHeight > duyuruContainers[1].offsetHeight) {
    duyuruContainers[1].style.height = duyuruContainers[0].offsetHeight + 'px'
}
else if (duyuruContainers[1].offsetHeight > duyuruContainers[0].offsetHeight) {
    duyuruContainers[0].style.height = duyuruContainers[1].offsetHeight + 'px'
}

