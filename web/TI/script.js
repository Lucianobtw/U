
function Gettime() {

  var insert = document.getElementById('Time')
  var today = new Date();
  var date = today.getDate() + '-' + today.getMonth() + '-' + today.getFullYear();
  var time = today.getHours() + ':' + today.getMinutes() + ':' + today.getSeconds();
  var DateHour = 'La fecha es: ' + date + '\nLa Hora es: ' + time;
  insert.innerText =  DateHour;
  return DateHour

}

function ZoomIn() {

  document.getElementById('lista').style.fontSize = '150%';
  return
}

function ZoomOut() {
  document.getElementById('lista').style.fontSize = '50%';
  return
}

function ZoomN() {
  document.getElementById('lista').style.fontSize = '100%';
  return
}


function displayI() {
  const imgI = document.getElementById('imgI');  
  imgI.style.display = 'block';
  return
}
function displayII() {
  const imgII = document.getElementById('imgII');
  imgII.style.display = 'block';
  return
}
function displayIII() {
  const imgIII = document.getElementById('imgIII');
  imgIII.style.display = 'block';
  return
}
function displayIV() {  
  const imgIV = document.getElementById('imgIV');
  imgIV.style.display = 'block';
  return
}
