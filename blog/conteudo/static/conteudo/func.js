

function clicar() {
}
function textos() {
    var text = document.getElementsByClassName("cont")
    if (text.length > 1) {
        for (var i=0; i<text.length; i++) {
            text[i].innerHTML = text[i].textContent
        }
    } else {
        text[0].innerHTML = text[0].textContent
    }
}
textos()