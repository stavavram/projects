var baseUrl = "http://localhost:5000/";

var getAllProjects = function () {
    //$("maindivid"). = "<div id=\"maindivid\"></div>";
    $.get(baseUrl + "get-projects", function(data, status){
        var obj = data;
        for(let singleValue of obj){
            $("#maindivid").append("<button class='btn btn-info' style='width: 20%' onclick='chooseProject($(this))'>" + singleValue + "</button>");
        }
    });
}

var chooseProject = function(event){
    projectName = event.text();
    document.getElementById("projectdivid").style.visibility = "visible";
    document.getElementById("maindivid").style.visibility = "hidden";
    document.getElementById("maindivid").style.height = "0%";
    $.get(baseUrl + "invoke-main?project=" + projectName, function (data, status) {
        console.log("invoke-main status code: " + status);
        let dataObj = data;
        for(let element of dataObj) {
            $("#tdbuttons").append(
                `<button class="btn btn-default" onclick="invokeFunction('${element.function_name}', '${projectName}')">${element.button_name}</button>`
            );
        }
    });
}

getAllProjects()