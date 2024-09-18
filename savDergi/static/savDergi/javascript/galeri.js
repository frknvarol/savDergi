const albumDiv = document.querySelectorAll('.album_div');

albumDiv.forEach(div => {
    div.addEventListener('click', () => {
        div.querySelector('.album_name a').click();
    })
});

albumDiv.forEach(div => {
   div.addEventListener('mouseover', () => {
       div.querySelector('.album_gallery-image').style.transition = "transform 150ms ease-in-out"
       div.querySelector('.album_gallery-image').style.transform = "scale(1.1)"
   })
});

albumDiv.forEach(div => {
   div.addEventListener('mouseout', () => {
       div.querySelector('.album_gallery-image').style.transition = "transform 75ms ease-in-out"
       div.querySelector('.album_gallery-image').style.transform = "scale(1)"
   })
});
