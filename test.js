var div  = document.body.children[0]
 var span = document.createElement('span')
  span.innerHTML = 'A new span!'
  div.appendChild(span)

document.write("<table>")
for(var i=0;i<100;i++){
document.write("<tr>"+i+"</tr>")
}
document.write("</table")


