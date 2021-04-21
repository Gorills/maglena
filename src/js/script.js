
$('.slider').slick({
   
    infinite: true,
    speed: 300,
    slidesToShow: 1,
    autoplay: true,
    prevArrow: "<div class='arrow-wrap prev'><i class='fas fa-long-arrow-alt-left '></i></div>",
    nextArrow: "<div class='arrow-wrap next'><i class='fas fa-long-arrow-alt-left '></i></div>",
  });

$(".menu-btn").click(function(e) {
    e.preventDefault();
    $(this).toggleClass('menu-btn_active');
    $(".header").toggleClass('header--active');
    $(".header__closer").toggleClass('header__closer--active');
});

$(".header__closer").click(function(e) {
    e.preventDefault();
    $(".menu-btn").removeClass('menu-btn_active');
    $(".header").removeClass('header--active');
    $(".header__closer").removeClass('header__closer--active');
});

$('.popup-btn').click(function(e){
    e.preventDefault();
    $('.popup').addClass('popup--active');
    $('.popup__closer').addClass('popup__closer--active');
});

$('.popup__closer').click(function(){
    $('.popup').removeClass('popup--active');
    $('.popup__closer').removeClass('popup__closer--active');

});

if( window.innerWidth > 768 ){
  $('.header__link-drop').hover(function(){
      $('.header__dropdown').addClass('header__dropdown--active')

  });

  $('.header__dropdown').mouseleave(function(){

          $(this).removeClass('header__dropdown--active')
  });
  } else {
      $('.header__link-drop').click(function(e){
          e.preventDefault();
          $('.header__dropdown').toggleClass('header__dropdown--active')
  
      });
  } 

jQuery(document).ready(function($) {
    var url=document.location.href;
    $.each($(".header__link"),function(){
        if(this.href==url){
            $(this).addClass('header__link--active');
        }
    });
});

jQuery(document).ready(function($) {
    var url=document.location.href;
    $.each($(".header__dropdown-link"),function(){
        if(this.href==url){
            $(this).addClass('header__dropdown-link--active');
            $('.header__link-drop').addClass('header__link--active')
        }
    });
});



