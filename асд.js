const carousel = document.querySelector('.u-carousel');
const carouselItems = document.querySelectorAll('.u-carousel-item');
const carouselInterval = 5000; 
let carouselIndex = 0;

function showSlide(index) 
{
  carouselItems.forEach(item => item.classList.remove('u-active'));
  carouselItems[index].classList.add('u-active');
}

function changeSlide(n) 
{
  carouselIndex += n;
  if (carouselIndex < 0) 
  {
    carouselIndex = carouselItems.length - 1;
  } 
  else if (carouselIndex >= carouselItems.length) 
  {
    carouselIndex = 0;
  }
  showSlide(carouselIndex);
}

function automaticSlide() 
{
  changeSlide(1);
}

let interval = setInterval(automaticSlide, carouselInterval);

carousel.addEventListener('mouseover', () => clearInterval(interval));
carousel.addEventListener('mouseleave', () => interval = setInterval(automaticSlide, carouselInterval));
document.querySelector('.u-carousel-arrow-left').addEventListener('click', () => 
{
  clearInterval(interval);
  changeSlide(-1);
});
document.querySelector('.u-carousel-arrow-right').addEventListener('click', () => 
{
  clearInterval(interval);
  changeSlide(1);
});



<div class="u-carousel-inner" role="listbox">
<div class="align-center section-3-1" src="">
  <div class="sheet">
    <h1 class="title">
      инж.Димитрина Цветкова</h1>
  </div>
</div>
<div class="align-center section-3-2" src="">
  <div class="sheet">
    <h1 class="title">инж.Пенка Янева</h1>
  </div>
</div>
<div class="align-center section-3-3" src="">
  <div class="sheet">
    <h1 class="title">инж.Ивайло Иванов</h1>
  </div>
</div>
<div class="align-center section-3-4" src="">
  <div class="sheet">
    <h1 class="title">инж.Елена Кацарска</h1>
  </div>
</div>
<div class="align-center section-3-5" src="">
  <div class="sheet">
    <h1 class="title">инж.Петър Петров</h1>
  </div>
</div>
</div>