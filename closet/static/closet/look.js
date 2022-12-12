document.addEventListener('DOMContentLoaded', () => {
    var closetpage = document.querySelector('#lookpage');
    closetpage.style.height = `${window.innerHeight -196}px`;
});

window.addEventListener('resize', () => {
    var closetpage = document.querySelector('#lookpage');
    closetpage.style.height = `${window.innerHeight -196}px`;
});