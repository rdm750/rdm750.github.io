$(document).ready(
//$('button').click(function(){
//var userChoice = $('prompt(""input[name=message]")'.val();
//}
var userChoice=prompt();
var test = document.getElementbyId('output').innerHTML; 
test.innerHTML=userChoice;

var computerChoice = Math.random();
if (computerChoice < 0.34) {
	computerChoice = "rock";
} else if(computerChoice <= 0.67) {
	computerChoice = "paper";
} else {
	computerChoice = "scissors";
} console.log("Computer: " + computerChoice);
test.innerHTML="Computer: " + computerChoice";


var compare = function(choice1, choice2) {
if (choice1 === choice2) {
return "The result is a tie!";
}

else if (choice1 === "paper") {
if (choice2 === "rock") {
return "paper wins";
}
else {
return "scissors wins";
}
}

else if(choice1=="scissors")
{
    if(choice2=="rock")
    return "rock wins";
    else if (choice2 == "paper")
    return "scissors wins";
}


else if (choice2 === "scissors") {
return "rock wins";
}
else {
return "paper wins";
}

};

var comp  = compare(userChoice,computerChoice);
console.log(comp);
test.innerHTML=comp;
);    
