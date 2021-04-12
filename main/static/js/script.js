console.log(121);
const headerLink = [...document.querySelectorAll('.header__item')];

function headerToggle(e) {
  for (let i = 0; i < headerLink.length; i++) {
    console.log(headerLink[i]);
    headerLink[i].addEventListener('click', function (e) {
      if (headerLink[i].classList.contains('header__item')) {
        headerLink.classList.remove('header__item');
        headerLink.classList.add('header__item-active'); // e.preventDefault()
      } else {
        headerLink.classList.remove('header__item-active');
        headerLink.classList.add('header__item');
      }
    });
  }
}

headerToggle();
const burger = document.querySelector('.burger');

if (burger) {
  const headerMenu = document.querySelector('.header__menu');
  burger.addEventListener('click', function (e) {
    document.body.classList.toggle('_lock');
    burger.classList.toggle('_active');
    headerMenu.classList.toggle('_active');
  });
}