function callback() {

}

// Define the onlick function
// Button activates callback function
//     reads users weight
//         validates that input is numeric
//             if not numeric: no fetch call
//             else: fetch call unitconv
//                 convert weight into t_oz
//                 extract weight from JSON
//                 multiply weight in t_oz by price of gold
//     create new div beneath input section
//         include time stamp
//         insert new divs into DOM so newer ones are first
//         if fetch() fails: display timestamped error message