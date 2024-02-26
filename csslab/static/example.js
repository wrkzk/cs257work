const the_heading = document.getElementById("hello");

function genNum() {
    let randNum = Math.floor(Math.random() * 100);
    the_heading.innerHTML = "Number: " + randNum;
}

genNum()