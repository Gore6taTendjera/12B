const goTopBtn = document.querySelector('.go-top-btn');
goTopBtn.style.display = "none";

window.addEventListener('scroll', checkHeight)

function checkHeight(){
  if(window.scrollY > 2800) {
    goTopBtn.style.display = "flex"
  } else {
    goTopBtn.style.display = "none"
  }
}

goTopBtn.addEventListener('click', () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  })
})