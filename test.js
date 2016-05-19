var $newdiv1 = $( "<div id='object1'/>" ),
  newdiv2 = document.createElement( "div" ),
  existingdiv1 = document.getElementById( "div" );
 
$( "body" ).append( $newdiv1, [ newdiv2, existingdiv1 ] ); 
