const portreDivs = document.querySelectorAll('.generic_div');

portreDivs.forEach(div => {
   div.addEventListener('click', () => {
       div.querySelector('.konferanslar_baslik').click();
   });
});