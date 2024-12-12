const makaleDiv = document.querySelectorAll('.makale_div');

makaleDiv.forEach(div => {
   div.addEventListener('click', () => {
       div.querySelector('.makale_baslik a').click();
   });
});