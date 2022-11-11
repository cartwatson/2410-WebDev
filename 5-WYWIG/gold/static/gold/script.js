// grab div blocks
const upperDiv = document.getElementById("upperDiv")
const lowerDiv = document.getElementById("lowerDiv")

// main.style.backgroundColor = "gray";

// Add price element to main
const priceBlock = document.createElement('p');
// Handle the 3 cases associated with gold prices
//             Request in process: display "Please Wait"
//             Request successful: display gold price
//             Request unsuccessful: display an error message
const priceText = document.createTextNode("TESTING");
priceBlock.style.textAlign = "center";
priceBlock.appendChild(priceText);
upperDiv.appendChild(priceBlock);
// upperDiv.innerHTML += priceBlock.innerHTML;


// Generate new div ---------------------------------------------------------------------------------------------------------------------
function callback(weight, unit, value) {
    // create new div
    const newDiv = document.createElement('div');
    // add timestamp
    const newSpan = document.createElement('span')
    const event = new Date();
    const options = { year: 'numeric', month: 'numeric', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric'};
    const date = event.toLocaleDateString(undefined, options);
    const dateNode = document.createTextNode(date + " -- ");
    newSpan.appendChild(dateNode);
    newDiv.appendChild(newSpan);
    
    var content;
    // handle errors
    if (weight === "" || unit === "" || weight.isNaN()) { // check for all error conditions
        newDiv.style.backgroundColor = "red";
        if (weight.isNaN()) { // validate weight is numeric
            content = document.createTextNode("Error! Weight needs to be a number!");
        } else { // didn't select a weight or unit
            content = document.createTextNode("Error! Invalid weight or unit!");
        }
    } else {
        // use selected color
        newDiv.style.backgroundColor = "blue";
        // compute price - parse unit
        var weigthInTOZ;
        switch (unit) {
            case "U.S. Ton (T)":
                // make request to unitconv
                break;
            case "Gram (g)":
                // make request to unitconv
                break;
            case "Troy Ounce (t_oz)":
                // make request to unitconv
                break;
            case "Kilogram (kg)":
                // make request to unitconv
                break;
            case "Imperial Pound (lb)":
                // make request to unitconv
                break;
            case "Ounce (oz)":
                // make request to unitconv for weight in TOZ
                break;
        }
        // TODO: handle case of failed fetch =========================================================================
        // calculate price
        price = weigthInTOZ * value;
        // print result
        content = document.createTextNode("Your weight of " + weight + " " + unit + " is " + weigthInTOZ + " Troy Ounces, and is worth $" + price + " USD with the current gold price.");
    }
    newDiv.appendChild(content);
    newDiv.style.textAlign = "Center";

    // onclick delete 
    newDiv.onclick = function() {this.remove();};

    // insert above existing results
    lowerDiv.insertBefore(newDiv, lowerDiv.firstChild);
}
