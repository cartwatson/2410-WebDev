// grab div block
const upperDiv = document.getElementById("upperDiv");

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
