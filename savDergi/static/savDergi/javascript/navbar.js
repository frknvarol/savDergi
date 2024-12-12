//NAVBAR DROPDOWN

const dropdown = document.querySelectorAll('.navbar_list-dropdown');

dropdown.forEach(ul => {
    ul.addEventListener('mouseover', () => {
        ul.querySelector('ul').classList.remove('hidden');
    });
});

dropdown.forEach(ul => {
    ul.addEventListener('mouseout', () => {
        ul.querySelector('ul').classList.add('hidden');
    });
});

//NAVBAR MOBILE


const navbarButton = document.querySelector('.navbar_button')
const navbarMobileContainer = document.querySelector('.navbar_mobile-container');
const navbarMobileButton = document.querySelector('.navbar_mobile-button');

navbarButton.addEventListener('click', () => {
    navbarMobileContainer.classList.remove('hidden');
});


navbarMobileButton.addEventListener('click', () => {
    navbarMobileContainer.classList.add('hidden');
});