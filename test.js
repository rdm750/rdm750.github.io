var $newdiv1 = "<div id='test'/>";
  newdiv2 = document.createElement( "div" );
  existingdiv1 = document.getElementById( "left" );
 
$( "test" ).append( $newdiv1, [ newdiv2, existingdiv1 ] ); 
