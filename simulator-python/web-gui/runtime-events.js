var baseUrl = "http://localhost:5000/";
var buttonsIds = ["btnPlay", "btnPlayOneStep", "btnStop"]
var round=0;
//var isAlreadyActive = false;
var runSampling = true;

var runSimulator = function () {
    //isAlreadyActive = true;
    blockButtons();
    $.get(baseUrl + "run", function (data, status) {
        startRoundSampling();
        console.log("run" + status);
        drawGraph();
    });
}

var runOneStep = function () {
    //isAlreadyActive = true;
    $.get(baseUrl + "run-single-step", function (data, status) {
        startRoundSampling();
        console.log("run-single-step" + status);
        drawGraph();
    });
}

var stop = function () {
    $.get(baseUrl + "stop", function (data, status) {
        startRoundSampling();
        console.log("stop" + status);
        unBlockButtons();
        drawGraph();
    });
}

var blockButtons = function(){
    for(let i=0; i < 2; i++){
        document.getElementById(buttonsIds[i]).disabled  = true;
        document.getElementById(buttonsIds[i]).style.opacity  = 0.4;
    }
}

var unBlockButtons = function(){
    for(let i=0; i < 2; i++){
        document.getElementById(buttonsIds[i]).disabled  = false;
        document.getElementById(buttonsIds[i]).style.opacity  = 1;
    }
};

var sendRoundSampling = function(){
    return new Promise((resolve, reject)=>{
        $.get(baseUrl + "get-rounds", async function (data, status) {
            document.getElementById("roundlable").innerText = data;
            resolve();
        });
    })
};

var startRoundSampling = async function() {
    await sendRoundSampling();
    //if(isAlreadyActive == false) {
        //while (runSampling) {

        //}
    //}
};

var invokeFunction = function (methodName, projectName) {
    $.get(baseUrl + `invoke-method?project=${projectName}&method=${methodName}`, function (data, status) {
        console.log("invoke-method status code: " + status);
    });
}
