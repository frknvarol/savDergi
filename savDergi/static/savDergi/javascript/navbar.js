//NAVBAR DROPDOWN

const kurumsal = document.querySelector('.navbar_kurumsal');
const dropdown = document.querySelector('.navbar_kurumsal-dropdown');


kurumsal.addEventListener('mouseover', () => {
    dropdown.classList.remove('hidden');
    }
);

kurumsal.addEventListener('mouseout', () => {
    dropdown.classList.add('hidden');
    }
);

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