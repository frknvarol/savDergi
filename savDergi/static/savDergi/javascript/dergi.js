const dergiDiv = document.querySelectorAll('.dergi_div');

dergiDiv.forEach(div => {
    div.addEventListener('click', () => {
        div.querySelector('.dergi_title a').click();
    })
});


dergiDiv.forEach(div => {
   div.addEventListener('mouseover', () => {
       div.style.transition = "transform 230ms ease-in-out"
       div.style.transform = "scale(1.02)"
   })
});

dergiDiv.forEach(div => {
   div.addEventListener('mouseout', () => {
       div.style.transition = "transform 170ms ease-in-out"
       div.style.transform = "scale(1)"
   })
});