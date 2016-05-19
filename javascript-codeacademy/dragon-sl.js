var slaying = true;
var youHit = Math.floor(Math.random() * 2);
var damageThisRound = Math.floor(Math.random()*5 + 1);
var totalDamage = 0;

while(slaying)
{
    if(youHit)
    {
    console.log("hit a dragon");
    document.write("<h1>hit a dragon<h1>");
    totalDamage += damageThisRound;
        if(totalDamage>=4)
        { 
            console.log("the player slew the dragon");
            document.write("<h1>hit a dragon<h1>");
            slaying =false;
        }
        else
            youHit = Math.floor(Math.random() * 2);    
    }
    else
    console.log("dragon defeated you");
    document.write("<p>dragon defeated you</p>");    
    
    slaying = false;
    }
