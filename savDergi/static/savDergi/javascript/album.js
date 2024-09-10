const albumImages = document.querySelectorAll('.album_image');
const docWidth = parseInt(window.getComputedStyle(document.querySelector('.album_header')).width.replace('px', ''))

albumImages.forEach(img => {
    const imgWidth = parseInt(window.getComputedStyle(img).width.replace('px', ''))

    let newWidth = String((docWidth - imgWidth) / 2) + 'px'
    img.addEventListener('click', () => {
        img.classList.add('album_clicked')
    });
});


