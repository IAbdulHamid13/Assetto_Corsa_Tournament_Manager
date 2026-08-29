// Set up header images
let headerImages = [];

function addHeaderImage(nameOfImage, posX = '50%', posY = '50%', size = '100%') {
    headerImages.push(`no-repeat url('/static/images/${nameOfImage}') ${posX} ${posY} / ${size}`);
}

addHeaderImage('header1.jpg');
addHeaderImage('header2.jpg', '50%', '58%');
addHeaderImage('header3.jpg', '50%', '60%');

// Header index
let currentHeaderIndex = 0;

function setHeaderImage(headerIndex = currentHeaderIndex) {
    let headers = document.querySelectorAll('header');
    headers.forEach(header => {
        header.style.background = headerImages[headerIndex];
    })
    currentHeaderIndex = (currentHeaderIndex + 1) % headerImages.length;
}

// DOMContentLoaded
function onDOMContentLoaded() {
    let startIndex = (Math.floor(Math.random() * 10)) % headerImages.length;
    setHeaderImage(startIndex);
    setInterval(setHeaderImage, 10000);
}

document.addEventListener('DOMContentLoaded', onDOMContentLoaded);