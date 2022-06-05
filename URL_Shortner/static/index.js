function copytext() {
    let htmlelement = document.getElementById("shortlink");
    // console.log(htmlelement.innerText);

    navigator.clipboard.writeText(htmlelement.innerText);
    var copiedtext = htmlelement.innerText;
    console.log(copiedtext);
}

copytext();