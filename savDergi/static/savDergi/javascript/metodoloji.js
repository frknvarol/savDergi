const portreDivs = document.querySelectorAll('.generic_div');

portreDivs.forEach(div => {
   div.addEventListener('click', () => {
       div.querySelector('.metodoloji_baslik').click();
   });
});