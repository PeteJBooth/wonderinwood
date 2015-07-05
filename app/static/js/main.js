$(document).ready(function(){
    //$('.overlay').hide();
    $('.nav-list .child-container').slideUp(0);
    $('.nav-list .nav-arrow').addClass('closed');
    $('.nav-list .nav-arrow').click(function(e){
        e.preventDefault();
        $(this).toggleClass('closed');
    	$(this).parent().siblings('.child-container').slideToggle(400);
    });

})