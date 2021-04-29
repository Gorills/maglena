
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

  if( window.innerWidth > 768 ){
        $('.closer').hover(function(){
            $('.header__dropdown').removeClass('header__dropdown--active')

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



$(window).scroll(function() {
    var height = $(window).scrollTop();
    /*Если сделали скролл на 100px задаём новый класс для header*/
    if(height > 125){
        $('.header').addClass('header--fixed');
        $('.margintop').addClass('margintop--active');
        
    } else{
        /*Если меньше 100px удаляем класс для header*/
        $('.header').removeClass('header--fixed');
        $('.margintop').removeClass('margintop--active');
    }
});

$('.work-grid').magnificPopup({
    delegate: 'a',
    // child items selector, by clicking on it popup will open
    type: 'image',
    gallery: {
      enabled: true,
      // set to true to enable gallery
      preload: [0, 2],
      // read about this option in next Lazy-loading section
      navigateByImgClick: true,
      arrowMarkup: '<button title="%title%" type="button" class="mfp-arrow mfp-arrow-%dir%"></button>',
      // markup of an arrow button
      tPrev: 'Previous (Left arrow key)',
      // title for left button
      tNext: 'Next (Right arrow key)',
      // title for right button
      tCounter: '<span class="mfp-counter">%curr% of %total%</span>' // markup of counter
  
    }
  });

  $('.tabs-wrapper').each(function() {
	let ths = $(this);
	ths.find('.tab-item').not(':first').hide();
	ths.find('.tab').click(function() {
		ths.find('.tab').removeClass('active').eq($(this).index()).addClass('active');
		ths.find('.tab-item').hide().eq($(this).index()).fadeIn()
	}).eq(0).addClass('active');
});

$(document).ready(function() {
    
    var classes = ['wow fadeIn', 'wow slideInDown', 'wow slideInDown', 'wow fadeIn', 'wow fadeIn'];
    $('.list-wrap__item').each(function(i) {
        $(this).addClass(
            classes[Math.floor(Math.random()*classes.length)]);
    });
    var title = ['wow bounceInLeft', 'wow backInDown', 'wow backInUp', 'wow fadeInDownBig', 'wow fadeInUpBig', 'wow'];
    $('h1').each(function(i) {
        $('h1').addClass(
            title[Math.floor(Math.random()*classes.length)]);
    });

    $('.standart img').each(function(i) {
        $('.standart img').addClass('wow fadeInDownBig');
    });
 
})




