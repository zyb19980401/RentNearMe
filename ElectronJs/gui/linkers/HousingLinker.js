
let { PythonShell } = require('python-shell')
var path = require("path")
let options = {}



function getData() {
    try {
        spinnerdiv = doucment,createElement("div")
        spinnerdiv.class = "spinner-border"
        spinnerdiv.style = "width: 3rem; height: 3rem;"
        spinnerdiv.role = "status"
        nextToButton = doucment.getElementById("nextTobody")
        nextToButton.appendChild(spinnerdiv)
        buyOrRent = document.getElementById("buyOrRentInput").value
        upperLimit = document.getElementById("upperLimit").value
        lowerLImit = document.getElementById("lowerLimit").value
        addressInput = document.getElementById("addressInput").value
        bedroomInput = document.getElementById("bedroomInput").value
        washroomInput = document.getElementById("washroomInput").value
        parkingInput = document.getElementById("parkingInput").value
        finalHtmlInput = [buyOrRent, upperLimit, lowerLImit, addressInput, bedroomInput, washroomInput, parkingInput]
        console.log(finalHtmlInput)
        options = {
            scriptPath: path.join(__dirname, '/../engine/'),
            //have to add a bracket, otherwise it will be 7 arguments
            args: [finalHtmlInput]
        }
    } catch{
        console.log("we do not have input here")
    }
    console.log("i am in get data")

    let pyshell = new PythonShell('script.py', options);


    pyshell.on('message', function (message) {
        var x = document.getElementsByTagName("BODY")[0];
        var divc = document.createElement("div");
        var h = document.createElement("h1");                // Create a <h1> element
        var t = document.createTextNode(message);     // Create a text node
        h.appendChild(t); 
        divc.appendChild(h);
        x.appendChild(divc);      
    })
}
