// Smooth scrolling for navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Sticky Navbar
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    navbar.classList.toggle('sticky', window.scrollY > 0);
});
