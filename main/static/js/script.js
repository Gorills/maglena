$('.slick').slick({
  infinite: true,
  speed: 1000,
  slidesToShow: 1,
  adaptiveHeight: true,
  autoplay: true,
  pauseOnFocus: false,
  pauseOnHover: false,
  pauseOnDotsHover: false,
  dots: true,
  prevArrow: "<i class=\"fas fa-angle-left prev\"></i>",
  nextArrow: "<i class=\"fas fa-angle-right next\"></i>"
});
$('.clients__slider').slick({
  infinite: true,
  speed: 300,
  slidesToShow: 1,
  adaptiveHeight: true,
  autoplay: true,
  pauseOnFocus: false,
  arrows: true
});
$(".menu-btn").click(function (e) {
  e.preventDefault();
  $(this).toggleClass('menu-btn_active');
  $(".header").toggleClass('header--active');
  $(".header__closer").toggleClass('header__closer--active');
});
$(".header__closer").click(function (e) {
  $(".menu-btn").removeClass('menu-btn_active');
  $(".header").removeClass('header--active');
  $(".header__closer").removeClass('header__closer--active');
});
$(".header__link").click(function (e) {
  $(".menu-btn").removeClass('menu-btn_active');
  $(".header").removeClass('header--active');
  $(".header__closer").removeClass('header__closer--active');
});
$(".top__link").click(function (e) {
  $(".menu-btn").removeClass('menu-btn_active');
  $(".header").removeClass('header--active');
  $(".header__closer").removeClass('header__closer--active');
});
$(window).scroll(function () {
  var height = $(window).scrollTop();
  /*Если сделали скролл на 100px задаём новый класс для header*/

  if (height > 500) {
    $('header').addClass('header--fixed');
    $('.slick').addClass('slick--active');
    $('.posadochnaya-start').addClass('posadochnaya-start--active');
  } else {
    /*Если меньше 100px удаляем класс для header*/
    $('header').removeClass('header--fixed');
    $('.slick').removeClass('slick--active');
    $('.posadochnaya-start').removeClass('posadochnaya-start--active');
  }
});
$("body").on('click', '[href*="#"]', function (e) {
  var fixed_offset = 120;
  $('html,body').stop().animate({
    scrollTop: $(this.hash).offset().top - fixed_offset
  }, 1000);
  e.preventDefault();
}); // Активная ссылка для header в зависимости от url

jQuery(document).ready(function ($) {
  var url = document.location.href;
  $.each($(".header__link"), function () {
    if (this.href == url) {
      $(this).addClass('header__link--active');
    }
  });
});
$('.show_popup').click(function (e) {
  // Вызываем функцию по нажатию на кнопку
  e.preventDefault();
  $('.popup').show(); // Открываем блок заднего фона

  $('.overlay_popup').show(); // Открываем блок заднего фона
});
$('.overlay_popup').click(function () {
  // Обрабатываем клик по заднему фону
  $('.overlay_popup, .popup').hide(); // Скрываем затемнённый задний фон и основное всплывающее окно
});
$('.social-popup__btn').click(function (e) {
  // Вызываем функцию по нажатию на кнопку
  e.preventDefault();
  $('.social-popup').toggleClass('social-popup--active'); // Открываем блок заднего фона

  $('.social-popup__overlay').toggleClass('social-popup__overlay--active'); // Открываем блок заднего фона

  $(this).toggleClass('social-popup__btn--active');
});
$('.social-popup__overlay').click(function () {
  $(this).removeClass('social-popup__overlay--active');
  $('.social-popup').removeClass('social-popup--active');
  $('.social-popup__btn').toggleClass('social-popup__btn--active');
});