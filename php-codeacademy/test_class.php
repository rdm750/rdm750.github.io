<!DOCTYPE html>
<html>
	<head>
	  <title>Reconstructing the Person Class</title>
      <link type='text/css' rel='stylesheet' href='style.css'/>
	</head>
	<body>
      <p>
        <!-- Your code here -->
      <?php
        class Person{
            public $isAlive = true;
            public $firstname;
            public $lastname;
            public $age;
            public function __construct($firstname,$lastname,$age){
             $this->firstname = $firstname;
             $this->lastname = $lastname;
             $this->age=$age;
            }
            public function greet(){
             return "Hello, my name is ".$this->firstname." " .$this->lastname.". Nice to meet you! :-)";   
            }
        
}
      class Person1{
       
       public static function say(){ echo "Here are my thoughts!";}   
      }
      
      class Blogger extends Person1{
          const cats = 50;
          
      }
      
      Person1::say();
      echo Blogger::cats;
      
        $teacher = new Person("boring", "12345", 12345);
        $student = new Person("bortestng", "145", 123);
        echo $student->age;
        echo $teacher->greet();
        echo $student->greet();
        ?>
      </p>
    </body>
</html>
