
let { PythonShell } = require('python-shell')
var path = require("path")
let options = {}



function getData() {
    upperLimit = document.getElementById("upperLimit").value
    lowerLImit = document.getElementById("lowerLimit").value
    addressInput = document.getElementById("addressInput").value
    lowerLImit = document.getElementById("lowerLimit").value
    bedroomInput = document.getElementById("bedroomInput").value
    washroomInput = document.getElementById("washroomInput").value
    parkingInput = document.getElementById("parkingInput").value
    finalHtmlInput =[upperLimit,lowerLImit,addressInput,lowerLImit,bedroomInput,washroomInput,parkingInput]
    options = {
        scriptPath: path.join(__dirname, '/../engine/'),
        //have to add a bracket, otherwise it will be 7 arguments
        args: [finalHtmlInput]
    }

    let pyshell = new PythonShell('script.py', options);


    pyshell.on('message', function (message) {
        console.log(message);
    })
}
