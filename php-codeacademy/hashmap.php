<html>
  <head>
    <title>I am the King of Arrays!</title>
  </head>
  <body>
    <p>
      <?php
      // On the line below, create your own associative array:
        $myArray = array('qwer'=>'2',
        'test'=>'t',
        'qwe'=>'1');

      // On the line below, output one of the values to the page:
        echo $myArray['qwer']."<br>";
          
      // On the line below, loop through the array and output
      // *all* of the values to the page:

     foreach ($myArray as $value=>$key){
      echo $value.' '.$key."<br>";  
     }
     
      ?>
    </p>
  </body>
</html>
