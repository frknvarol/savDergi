const images = document.querySelectorAll('.metodoloji-instance_img');
const container = document.querySelector('.generic_container');
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


images.forEach(img => {
    img.addEventListener('click', () => {
        clickedImage.src = img.src
        container.appendChild(clickedImageDiv)
    });
});

clickedImageDiv.addEventListener('click', () => {
    container.removeChild(clickedImageDiv)
})
