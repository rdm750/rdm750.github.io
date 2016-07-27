dy(function(){

  $('div, #fixedbar a').hover(
    function(){
    $(this).addClass('active');
    },
    function(){
        $(this).removeClass('active');
    }
  );

});
