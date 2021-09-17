server = "http://127.0.0.1:8000/"

function ajax(method, path, callFunction) {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        console.log(path)
        if (callFunction != null)
            callFunction(JSON.parse(this.responseText))
    };
    xhttp.open(method, server + path, false);
    xhttp.send();
}