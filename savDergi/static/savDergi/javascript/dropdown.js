const kurumsal = document.querySelector('.navbar_kurumsal')
const dropdown = document.querySelector('.navbar_kurumsal-dropdown')
console.log(kurumsal)


kurumsal.addEventListener('mouseover', function(e) {
    dropdown.classList.remove('hidden')
    }
)

kurumsal.addEventListener('mouseout', function(e) {
    dropdown.classList.add('hidden')
    }
)