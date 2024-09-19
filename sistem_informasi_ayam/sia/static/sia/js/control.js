const nav_dropdown = document.querySelector('.nav-dropdown')  
const hamburger = document.querySelector('.hamburger')  

function toggleDropdown() {
    const nav_dropdown = document.querySelector('.nav-dropdown');
    nav_dropdown.classList.toggle('show');

    const hamburgerIcon = document.getElementById('hamburgerIcon')

    if (hamburgerIcon.classList.contains('fa-bars')){
        hamburgerIcon.classList.remove('fa-bars')
        hamburgerIcon.classList.add('fa-x')
    }else {
        hamburgerIcon.classList.remove('fa-x')
        hamburgerIcon.classList.add('fa-bars')
    }
}

window.addEventListener('scroll',(e)=>{
    const nav = document.querySelector('.header-color');
    if(window.scrollY>0){
        nav.classList.toggle('addShadow-scroll')
    }
});