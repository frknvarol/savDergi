const albumImages = document.querySelectorAll('.album_image');
const album = document.querySelector('.album');
const body = document.querySelector('body')
const html = document.querySelector('html')
const fullHeight = String(Math.max(body.scrollHeight, body.offsetHeight,
  html.clientHeight, html.scrollHeight, html.offsetHeight)) + 'px';

const clickedImageDiv = document.createElement('div');
const clickedImageFigure = document.createElement('figure');
const clickedImage = document.createElement('img');

clickedImageFigure.classList.add('album_clicked-figure')
clickedImage.classList.add('album_clicked-img')

clickedImageDiv.appendChild(clickedImageFigure)
clickedImageFigure.appendChild(clickedImage)

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
