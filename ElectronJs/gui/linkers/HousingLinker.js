
let { PythonShell } = require('python-shell')
var path = require("path")
let options = {}
let spinneradded = false

function getClicked(){
    if(spinneradded == false){
        addSpinner()
        addTable()
        getData()
        spinneradded= true
    }
    else(
        getData()
    )

}


function getData() {
    try {
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
        console.log(message + 32323)
        acc = message.split(",")
        console.log(acc + 32323)
        Price = acc[0].slice(1)
        address = acc[1] + acc[2]
        bedRoomNum = acc[3]
        washRommNum = acc[4]
        ParkingInfo = acc[5]
        Link = acc[7]
        ManagementFee = acc[8].slice(0,-1)
        Size = acc[6]
        table = document.getElementById("tableBody")

        let instructionRow = document.createElement("tr");

      
    
        let cellPrice = document.createElement("td");
        let cellPriceText = document.createTextNode(Price);
        cellPrice.appendChild(cellPriceText);
        instructionRow.appendChild(cellPrice);
    
        let cellAdress = document.createElement("td");
        let cellAdressText = document.createTextNode(address);
        cellAdress.appendChild(cellAdressText);
        instructionRow.appendChild(cellAdress);
    
        let cell5 = document.createElement("td");
        let cell5Text = document.createTextNode(bedRoomNum);
        cell5.appendChild(cell5Text);
        instructionRow.appendChild(cell5);
    
        let cellwashRoom = document.createElement("td");
        let cellWashRoomText = document.createTextNode(washRommNum);
        cellwashRoom.appendChild(cellWashRoomText);
        instructionRow.appendChild(cellwashRoom);
    
        let cellParking = document.createElement("td");
        let cellParkingText = document.createTextNode(ParkingInfo);
        cellParking.appendChild(cellParkingText);
        instructionRow.appendChild(cellParking);

        let cellSize = document.createElement("td");
        let cellSizeText = document.createTextNode(Size);
        cellSize.appendChild(cellSizeText);
        instructionRow.appendChild(cellSize);


        
        let cellManagement = document.createElement("td");
        let cell1ManagementText = document.createTextNode(ManagementFee);
        cellManagement.appendChild(cell1ManagementText);
        instructionRow.appendChild(cellManagement);
    
        let cellLink = document.createElement("td");
        let cellLinkText = document.createTextNode(Link);
        cellLink.appendChild(cellLinkText);
        instructionRow.appendChild(cellLink);


        table.appendChild(instructionRow)
    })
}
function addSpinner(){
    spinnerText = document.createTextNode("Loading...")
    spinnerdiv = document.createElement("div")
    spinnerdiv.className = "spinner-border"
    spinnerdiv.style = "width: 3rem; height: 3rem; position: absolute; left: 60%;"
    spinnerdiv.role = "status"
    spanSpinner = document.createElement("span")
    spanSpinner.className = "sr-only"
    spanSpinner.width= width="50%"
    spanSpinner.appendChild(spinnerText)
    spinnerdiv.appendChild(spanSpinner)
    nextToButton = document.getElementsByTagName("BODY")[0]
    nextToButton.appendChild(spinnerdiv)
}

function addTable(){
    let body = document.getElementsByTagName("body")[0];

    // create elements <table> and a <tbody>
    let tbl = document.createElement("table");
    // tbl.width = "400"
    tbl.style = "position: absolute; left: 20%"
    var tblBody = document.createElement("tbody");
    tblBody.id = "tableBody"
  
    // cells creation
    // for (var j = 0; j <= 0; j++) {
      // table row creation
    let instructionRow = document.createElement("tr");
    // let cell1 = document.createElement("td");
    // let cell1Text = document.createTextNode("RentOrBuy");
    // cell1.appendChild(cell1Text);
    // instructionRow.appendChild(cell1);

    // let cell2 = document.createElement("td");
    // let cell2Text = document.createTextNode("LimitUpper");
    // cell2.appendChild(cell2Text);
    // instructionRow.appendChild(cell2);
  

    let cell3 = document.createElement("td");
    let cell3Text = document.createTextNode("Price");
    cell3.appendChild(cell3Text);
    instructionRow.appendChild(cell3);

    let cell4 = document.createElement("td");
    let cell4Text = document.createTextNode("address");
    cell4.appendChild(cell4Text);
    instructionRow.appendChild(cell4);

    let cell5 = document.createElement("td");
    let cell5Text = document.createTextNode("bedRoomNum");
    cell5.appendChild(cell5Text);
    instructionRow.appendChild(cell5);

    let cell6 = document.createElement("td");
    let cell6Text = document.createTextNode("washRommNum");
    cell6.appendChild(cell6Text);
    instructionRow.appendChild(cell6);

    let cell7 = document.createElement("td");
    let cell7Text = document.createTextNode("ParkingInfo");
    cell7.appendChild(cell7Text);
    instructionRow.appendChild(cell7);


    let cellSize = document.createElement("td");
    let cellSizeText = document.createTextNode("Size");
    cellSize.appendChild(cellSizeText);
    instructionRow.appendChild(cellSize);



    let cellManagement = document.createElement("td");
    let cell1ManagementText = document.createTextNode("ManagementFee");
    cellManagement.appendChild(cell1ManagementText);
    instructionRow.appendChild(cellManagement);

    let cellLink = document.createElement("td");
    let cellLinkText = document.createTextNode("Link");
    cellLink.appendChild(cellLinkText);
    instructionRow.appendChild(cellLink);

  
    tblBody.appendChild(instructionRow);
    tbl.appendChild(tblBody);
    body.appendChild(tbl);
    tbl.setAttribute("border", "2");
    tbl.setAttribute("width", "1200");
}
    //   for (var i = 0; i < 7; i++) {
    //     // create element <td> and text node 
    //     //Make text node the contents of <td> element
    //     // put <td> at end of the table row
    //     var cell = document.createElement("td");
    //     var cellText = document.createTextNode("cell is row " + j + ", column " + i);
  
    //     cell.appendChild(cellText);
    //     row.appendChild(cell);
    //   }
  
    //   //row added to end of table body
    //   tblBody.appendChild(row);
    // }
  
    // // append the <tbody> inside the <table>
    // tbl.appendChild(tblBody);
    // // put <table> in the <body>
    // body.appendChild(tbl);
    // // tbl border attribute to 
    // tbl.setAttribute("border", "2");
// }
