// get necessary elements
const lowerDiv = document.getElementById("lowerDiv");

// Generate new div
function callback(weight, unit) {
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
    if (weight === "" || unit === "" || weight.isNaN || weight < 0) { // check for all error conditions
        newDiv.style.backgroundColor = "red";
        // find error condition
        if (weight.isNaN) { // validate weight is numeric
            content = document.createTextNode("Error! Weight needs to be a number!");
        } else if (weight < 0) { // validate weight is a positive number
            content = document.createTextNode("Error! Weight needs to be a non-negative number!");
        } else { // didn't select a weight and/or unit
            content = document.createTextNode("Error! Invalid weight or unit!");
        }
    } else {
        // use selected color
        newDiv.style.backgroundColor = "gray";
        // compute price - parse unit
        var weigthInTOZ;
        var conversionFactor;
        switch (unit) {
            // make request to unitconv for conversion factor 
            case "U.S. Ton (T)":        conversionFactor ; break;
            case "Gram (g)":            conversionFactor ; break;
            case "Troy Ounce (t_oz)":   conversionFactor = 1; break;
            case "Kilogram (kg)":       conversionFactor ; break;
            case "Imperial Pound (lb)": conversionFactor ; break;
            case "Ounce (oz)":          conversionFactor ; break;
        }
        // TODO: handle case of failed fetch =========================================================================
        // get weight in T_Oz 
        weigthInTOZ = weight * conversionFactor
        // calculate value
        value = weigthInTOZ * price;
        // print result
        content = document.createTextNode("Your weight of " + weight + " " + unit + " is " + weigthInTOZ
            + " Troy Ounces, and is worth $" + value + " USD with the current gold price.");
    }
    newDiv.appendChild(content);
    newDiv.style.textAlign = "Center";

    // onclick delete 
    newDiv.onclick = function() { this.remove(); };

    // insert above existing results
    lowerDiv.insertBefore(newDiv, lowerDiv.firstChild);
}
