$(document).ready(function(){

$('button').click(function(){
Get_Data();
}
);



function Get_Data(){

var x;

if('weather_current'==$("#Opt").find("option:selected").val())
{
   x = 'http://api.apixu.com/v1/current.json?key=dc9e7f1f5fa84d4aa80193340162710&q='+$("#Zip").val();

}

else if('weather_forecast'==$("#Opt").find("option:selected").val()) {
    x = 'http://api.apixu.com/v1/forecast.json?key=dc9e7f1f5fa84d4aa80193340162710&q='+$("#Zip").val()+',days=7';

}
else if('weather_search'==$("#Opt").find("option:selected").val()) {
   x = 'http://api.apixu.com/v1/search.json?key=dc9e7f1f5fa84d4aa80193340162710&q='+$("#Zip").val();

}
else if('weather_history'==$("#Opt").find("option:selected").val()) {
    x = 'http://api.apixu.com/v1/history.json?key=dc9e7f1f5fa84d4aa80193340162710&q='+$("#Zip").val()+'&dt='+$('#hist').val();

}

console.log(x);  //working




    $.ajax(
    {
            url: x, 
            // local json file works in firefox not in chrome;
            //place html,css,test_script in same folder and open test_septa_.html 
            type: "GET", //GET  Read REST API 
            dataType: "json",
            error: function(data){

              $("#fare").text("ERROR! Unable to load JSON FIle");
            },
            success: function(data) {

                console.log(JSON.stringify(data));
                $('#data').empty();
                print_json(data);

                



            },
});

function print_json(json_data){
if (typeof(json_data) == 'object'){
   for (var s in json_data){
          if (JSON.stringify(s).includes('png')){
          $('#data').append('<div type='+'data>' + '<img src='+JSON.stringify(s).replace(/\"/g,'')+'>');
          }
          else{
          $('#data').append('<div type='+'data>' + JSON.stringify(s).replace(/\"/g,''));
          }
          console.log(JSON.stringify(s));
          print_json(json_data[s]);
   }
}
else{
  if (JSON.stringify(json_data).includes('png')){
  $('#data').append('<img src=http://' + JSON.stringify(json_data).substring(3,JSON.stringify(json_data).length-1) + '>' + '</div>');
  }

  else{
    $('#data').append(' :: ' + JSON.stringify(json_data).replace(/\"/g,'') + '</div>'+'<br>');
  }
 console.log(JSON.stringify(json_data));
}

} 
    


  }

});