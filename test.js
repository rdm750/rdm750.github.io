var div  = document.body.children[0]
 var span = document.createElement('span')
  span.innerHTML = 'A new span!'
  div.appendChild(span)

document.write("<table><tr><th>ID</th><th>Data</th></tr>")
for(var i=0;i<100;i++){
document.write("<tr><td>"+i+"</td><td>"+i**2+"</td></tr>")
}
document.write("</table")


