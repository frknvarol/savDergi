const portreDivs = document.querySelectorAll('.portre_div');

portreDivs.forEach(div => {
   div.addEventListener('click', () => {
       div.querySelector('.portre_baslik').click();
   });
});