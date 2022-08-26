function show(id) {
    
    const x = document.getElementById(id);

    if (x.style.display === 'none') {
        x.style.display = 'block';
    } else if (x.style.display === 'block') { 
        x.style.display = 'none';
    } else { 
        x.style.display = 'block';
    }
} 

function background(id, ruta) {
    const x = document.getElementById(id);
    x.style.backgroundImage = "url("+ruta+")";
    x.style.transition = '0.5s';
    return
}