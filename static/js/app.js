// Grab all modal elemnts using ID's
const modal = document.getElementById("modal");
const openBtn = document.getElementById("open-btn");
const closeBtn = document.getElementById("close-btn");

openBtn.addEventListener('click', ()=> {
    modal.style.display = "block"
})

closeBtn.addEventListener('click', ()=> {
    modal.style.display = "hidden"
})