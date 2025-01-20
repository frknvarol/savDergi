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


const duyuruContainers = document.querySelectorAll('.duyuru-sayi_container')



if (duyuruContainers[0].height > duyuruContainers[1]) {
    duyuruContainers[1].style.height = duyuruContainers[0].offsetHeight + 'px'
}
else {
    duyuruContainers[0].style.height = duyuruContainers[1].offsetHeight + 'px'
}

