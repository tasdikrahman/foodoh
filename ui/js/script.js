$('.carousel').carousel({
        interval: 2000
    })

$(document).ready(function(){
	
	$("#btn1,#button1").click(function() {
    var offset = 20; //Offset of 20px
	$('html, body').animate({
        scrollTop: $("#nav-bloc").offset().top + offset
    }, 2000);
});

	$("#btn2,#button2").click(function() {
    var offset = 20; //Offset of 20px
	$('html, body').animate({
        scrollTop: $("#mid_section").offset().top + offset
    }, 2000);
});

	$("#btn3,#button3").click(function() {
    var offset = 20; //Offset of 20px
	$('html, body').animate({
        scrollTop: $("#mid_section2").offset().top + offset
    }, 2000);
});

	$("#btn4,#button4").click(function() {
    var offset = 20; //Offset of 20px
	$('html, body').animate({
        scrollTop: $("#footer").offset().top + offset
    }, 2000);
});

$('#characterLeft').text('140 characters left');
    $('#message').keydown(function () {
        var max = 140;
        var len = $(this).val().length;
        if (len >= max) {
        alert('You have reached the character limit');            
        } 
        
    });    

});