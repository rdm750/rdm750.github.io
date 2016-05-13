var friends = {
    bill: {
        firstName: "Bill",
        lastName: "Gates",
        number: "(206) 555-5555",
        address: ['One Microsoft Way','Redmond','WA','98052']
    },
    steve: {
        firstName: "Steve",
        lastName: "hello",
        number: "123",
        address: ['123 hello Street', 'City', 'State']
    }
};

var list = function(friends){
    
    for (var friends in friends)
    {
        console.log(friends);
        
        }
    };
    
    var search = function(name) {
    for(var key in friends) {
        if(friends[key].firstName === name) {
            console.log(friends[key]);
            return friends[key];
        }
    }
};
    list(friends);
    
