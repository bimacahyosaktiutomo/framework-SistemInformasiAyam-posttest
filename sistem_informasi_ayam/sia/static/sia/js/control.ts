
function toggleDropdown(): void {
    const hamburgerIcon = document.getElementById('hamburgerIcon') as HTMLElement;
    hamburgerIcon.classList.toggle('rotate');
    // const nav_dropdown = document.querySelector('.nav-dropdown') as HTMLElement;
    // nav_dropdown.classList.toggle("show");

    if (hamburgerIcon.classList.contains('fa-bars')) {
        hamburgerIcon.classList.remove('fa-bars');
        hamburgerIcon.classList.add('fa-x');
    } else {
        hamburgerIcon.classList.remove('fa-x');
        hamburgerIcon.classList.add('fa-bars');
    }
}

function PreviewImage(): void{
    const fileInput = document.getElementById('id_image') as HTMLInputElement;

    if (fileInput.files) {
        const oFReader = new FileReader();
        oFReader.readAsDataURL(fileInput.files[0]);

        oFReader.onload = function (oFREvent) {
            const imgPreview = document.getElementById('imgPreview') as HTMLImageElement | null;
            if (imgPreview && oFREvent.target) {
                imgPreview.src = oFREvent.target.result as string;
            }
        };
    };
}

document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        const alert = document.querySelector('.info-alert') as HTMLElement;
        if (alert) {
            setTimeout(() => {
                alert.classList.add('fade');
            }, 500)
            setTimeout(() => {
                alert.style.display = 'none';
            }, 1000)
        }
    }, 3000)
})

window.addEventListener('scroll', (e: Event): void => {
    const nav = document.querySelector('.header-color') as HTMLElement;
    if (window.scrollY > 0) {
        nav.classList.toggle('addShadow-scroll');
    }
});
