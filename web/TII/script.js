
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

function backgroundI(id) {
    const x = document.getElementById(id);
    x.style.backgroundImage = "url('./img/imgI.jpg')";
    x.style.transition = '0.5s';
    return
}

function backgroundII(id) {
    const x = document.getElementById(id);
    x.style.backgroundImage = "url('./img/imgII.jpg')";
    x.style.transition = '0.5s';
    return
}

function backgroundIII(id) {
    const x = document.getElementById(id);
    x.style.backgroundImage = "url('./img/imgIII.jpg')";
    x.style.transition = '0.5s';
    return
}

function backgroundIV(id) {
    const x = document.getElementById(id);
    x.style.backgroundImage = "url('./img/imgIV.jpg')";
    x.style.transition = '0.5s';
    return
}

function backgroundV(id) {
    const x = document.getElementById(id);
    x.style.backgroundImage = "url('./img/imgV.jpg')";
    x.style.transition = '0.5s';
    return
}