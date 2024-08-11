const figure = document.querySelectorAll('.album_figure')

figure.forEach(figure => {
    const image = figure.querySelector('.album_image')
    figure.style.height = image.offsetHeight + 'px'

})