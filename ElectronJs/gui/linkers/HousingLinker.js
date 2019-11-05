
let { PythonShell } = require('python-shell')
var path = require("path")
let options = {}



function getData() {
    buyOrRent = document.getElementById("buyOrRentInput").value
    upperLimit = document.getElementById("upperLimit").value
    lowerLImit = document.getElementById("lowerLimit").value
    addressInput = document.getElementById("addressInput").value
    bedroomInput = document.getElementById("bedroomInput").value
    washroomInput = document.getElementById("washroomInput").value
    parkingInput = document.getElementById("parkingInput").value
    finalHtmlInput =[buyOrRent,upperLimit,lowerLImit,addressInput,bedroomInput,washroomInput,parkingInput]
    console.log(finalHtmlInput)
    options = {
        scriptPath: path.join(__dirname, '/../engine/'),
        //have to add a bracket, otherwise it will be 7 arguments
        args: [finalHtmlInput]
    }
    console.log("i am in get data")

    let pyshell = new PythonShell('script.py', options);


    pyshell.on('message', function (message) {
        console.log(message);
    })
}
