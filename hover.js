dy(function(){

  $('#navigation a, #fixedbar a').hover(
    function(){
    $(this).addClass('active');
    },
    function(){
        $(this).removeClass('active');
    }
  );

});
