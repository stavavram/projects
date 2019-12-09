var baseUrl = "http://localhost:5000/";
var currentProject = ""

var getAllProjects = function () {
    $.get(baseUrl + "get-projects", function(data, status){
        for(let singleValue of data){
            $("#projectlistid").append("<li><button class='button primary' onclick='setCurrentProject($(this))'>" +  singleValue + "</button></li>");
        }
    });
}

var setCurrentProject = function(event){
    currentProject = event.text();
}

var chooseProject = function(){
    if(currentProject !== "") {
        cleanDiv("projectbuttons")
        $.get(baseUrl + "invoke-main?project=" + currentProject, function (dataStr, status) {
            console.log("invoke-main status code: " + status);
            if (dataStr) {
                data = JSON.parse(dataStr)
                for (let buttonName of Object.keys(data)) {
                    $("#projectbuttons").append(
                        `<button type="button" class="btn btn-default" data-toggle="modal" data-target="#myModal" onclick="prepareModal('${buttonName}')">${buttonName}</button>`
                    );
                }
                methodsData = data;
            }
        });
    }
    else {
        alert("Please Choose A Project")
    }
}

var prepareModal = function(methodName){
    $("#modalheader").text(methodName)
    cleanDiv("paramsid");
    params = methodsData[methodName]
    for(let paramKey in params) {
        $("#paramsid").append(
            `<div style="margin-bottom:3%">` +
            `<label class="paramsforpassing" style="color:black">name: ${params[paramKey].name}</label> ` +
            `<label style="color:black">description: ${!params[paramKey].description ? "Empty": params[paramKey].description}</label> ` +
            `<input class="paramsforpassing" style="width: 150px;color:black"/>` +
            `</div>`
        )
    }
    $("#paramsid").append(`<div><button type="button" class="btn btn-info" onclick="invokeProjectMethod('${currentProject}', '${methodName}')">Activate</button></div>`)
}

var cleanDiv = function(id){
  const myNode = document.getElementById(id);
  myNode.innerHTML = '';
}

getAllProjects()