// get ip

// get location from FreeGeoIP.app
// init vars
var city;
var region;
var country;
var locationLoaded = 0;

// 0ow9x2FVmLjrfqF7eDQJD0PKsd4tafyhFtLYlWCP
//var locationURL = "https://api.ipbase.com/v2/info?apikey=0ow9x2FVmLjrfqF7eDQJD0PKsd4tafyhFtLYlWCP&ip=1.1.1.1";
var weatherURL = "";
fetch(locationURL)
    .then(response => response.json())
    .then(json => {
        // pull out just the USD curr price
        city = json.data.location.city.name;
        region = json.data.location.region.name;
        country = json.data.location.country.name;
    })
    .catch(err => {
        priceMessage.innerHTML = "Error retrieving price of gold! Try again later!";
    })
    // get weather info from OpenWeatherMap
    .then(json2 => {
        return fetch(weatherURL);
    })
    .then()
    .catch(err => {

    })
    .then()

// put location and weather into 

// DOM Manager
const LocationDiv = Vue.createApp({
    data() {
        return {
            // conditions
                //  0 - not yet loaded
                //  1 - loaded
                // -1 - error in loading
            locationLoaded: locationLoaded, 
            weatherLoaded: 1,
            // data
            // -- location data
            nameOfLocation: "Logan, Utah, United States",
            coordinates: "patooey",
            // -- weather data
            // TODO: actually get currConditions
            date: "3/3/3333 9:08:59 PM",
            temperature: '38.59',
            tempHigh: '46.4',
            tempLow: '33.01',
            conditions: "clear sky",
            humidity: '61',
            pressure: '1023',
            // forecasts
            unlikelyCounter: 0,
            neutralCounter: 0,
            likelyCounter: 0,
                //  1 - likely
                //  0 - neutral
                // -1 - unlikely
            forecasts: [
                {likelyness: '1', date: '3/3/3333 12PM', temperature: '34.4', conditions: 'broken clouds', humidity: '97', pressure: '1026'},
            ]
        }
    },
}).mount('#app')