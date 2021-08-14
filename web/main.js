function startListening(){
    var sens = document.getElementById("sens").value
    eel.main(sens)(showOutput)
}

function termPy(){
    eel.terminatePython()
}

eel.expose(showOutput);
function showOutput(out){
    document.getElementById("text").style.display='block';
    document.getElementById("text").innerHTML = out;

}