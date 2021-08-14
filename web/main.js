function startListening(){
    var sens = document.getElementById("sens").value
    eel.main(sens)(showOutput)
}

var count = 0

function interfacePython(){
    if (count == 0){
        startListening()
        document.getElementById("toggleButton").className = "btn btn-danger"
        document.getElementById("toggleButton").innerHTML = "Stop Listening"
        document.getElementById("text").style.display='block';
        
    }
    else if (count%2==1){
        document.getElementById("toggleButton").className = "btn btn-primary"
        document.getElementById("toggleButton").innerHTML = "Start Listening"
        document.getElementById("text").style.display='none';
        termPy()
    }
    else if(count%2 == 0 ){
        document.getElementById("toggleButton").className = "btn btn-danger"
        document.getElementById("toggleButton").innerHTML = "Stop Listening"
        document.getElementById("text").style.display='block';
        termPy()
    }
    count++
}

function termPy(){
    var sens = document.getElementById("sens").value
    console.log(sens)
    eel.togglePython(sens)
}

eel.expose(showOutput);
function showOutput(out){
    document.getElementById("text").style.display='block';
    document.getElementById("text").innerHTML = out;

}