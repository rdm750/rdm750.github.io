dy(function(){

  $('#navigation, #fixedbar a').hover(
    function(){
    $(this).addClass('active');
    },
    function(){
        $(this).removeClass('active');
    }
  );

});
