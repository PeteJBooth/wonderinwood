$(document).ready(function(){
    $('.nav-list .child-container').slideUp(0);
    $('.nav-list .nav-arrow').addClass('closed');
    
    //re-open any current menu items and their parents
    $active = $('.nav-list .link_container.current');
    while(true){
        $active.parent().slideDown(0);
    	if ($active.parent('.child-container').length >0){
    		$active.parent('.child-container').slideDown(0);
    		$active = $('#cat-' + $active.parent().data('child-of'));
    		continue;
    	}
    	break;

    }
    $('.nav-list .nav-arrow').click(function(e){
        e.preventDefault();
        $(this).toggleClass('closed');
    	$(this).parent().next('.child-container').slideToggle(400);
    });

})