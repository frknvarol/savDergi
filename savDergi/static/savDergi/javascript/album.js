const albumImages = document.querySelectorAll('.album_image');
const album = document.querySelector('.album');
const fullHeight = String(document.querySelector('body').scrollHeight) + 'px';

const clickedImageDiv = document.createElement('div');
const clickedImage = document.createElement('img');
clickedImageDiv.appendChild(clickedImage)

clickedImageDiv.classList.add('album_clicked');
clickedImageDiv.style.height = fullHeight;


albumImages.forEach(img => {
    img.addEventListener('click', () => {
        clickedImage.src = img.src
        album.appendChild(clickedImageDiv)
    });
});

clickedImageDiv.addEventListener('click', () => {
    album.removeChild(clickedImageDiv)
})
