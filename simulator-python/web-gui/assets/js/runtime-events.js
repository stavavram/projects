var baseUrl = "http://localhost:5000/";
var buttonsIds = ["btnPlay", "btnPlayOneStep", "btnStop"]

var round=0;
var methodsData = {}

var runSimulator = function () {
    $loading.show();
    blockButtons();
    $.get(baseUrl + "run", function (data, status) {
        startRoundSampling();
        console.log("run" + status);
        drawGraph();
        $loading.hide();
    });
}

var runOneStep = function () {
        $loading.show();
    $.get(baseUrl + "run-single-step", function (data, status) {
        startRoundSampling();
        console.log("run-single-step" + status);
        drawGraph();
            $loading.hide();
    });
}

var stop = function () {
    $.get(baseUrl + "stop", function (data, status) {
        startRoundSampling();
        console.log("stop" + status);
        unBlockButtons();
        drawGraph();
        $loading.hide();
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
};

var invokeProjectMethod = function(projectName, methodName){
    let reqBody = {}
    let contents = $(".paramsforpassing");
    for(let i=0; i< contents.length; i+=2){
        let paramName = contents[i].textContent.split("name:")[1].trim();
        reqBody[paramName] = contents[i+1].value;
    }
    reqBody["project"] = projectName;
    reqBody["method"] = methodName;
    $.ajax({
        url: baseUrl + `invoke-method`,
        contentType: "application/json; charset=utf-8",
        dataType: 'json',
        type: 'POST',
        data: JSON.stringify(reqBody),
        success: function(data){
          console.log('succes: '+data);
          $("#myModal").modal("toggle")
            drawGraph();
        },
        error: function(XMLHttpRequest, textStatus, errorThrown){
            console.log('error: '+ XMLHttpRequest.responseJSON);
            alert(`Error thrown. message: ${XMLHttpRequest.responseJSON}`)
        }
  });
}