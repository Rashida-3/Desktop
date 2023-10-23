// now we need to datermine the constant of one of the id function.
// because no HTML function can be used directly on javascript

var inputval = document.querySelector("#cityinput");
var btn = document.querySelector("#add");
var city = document.querySelector("#cityoutput");
var descrip = document.querySelector("#description");
var temp = document.querySelector("#temp");
var wind = document.querySelector("#wind");
// api link id

apik = "d4f531be8e2fb8b34fb4978e6af0d5eb"
// kelvin to celcious. 1 kelvin is equal tp 272.15 celsius

function convertion(val) {
    return (val - 273).toFixed(2)
}
// Now we have to collect all the information with the help of fetch method

btn.addEventListener('click', function () {
    console.log(inputval.value)
    // this is the link from where all the information will be collected
    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${inputval.value}'&appid='${apik}`)

        .then(res => res.json())
        // then (data => consol.log (data))
S
        .then(data => {
            // now you need to collect the necessary information with the API link.
            console.log(data)
            // now i will collect that data and store it in defferent constants

            var nameval = data['name']
            var descrip = data['weather'][0]['description']
            var tempature = data['main']['temp']
            var wndspd = data['wind']['speed']
            // now with the help of innerHTML you have to make arrangements to display all the information in the webpage.
            city.innerHTML = `Weather of <span> ${nameval}</span>`
            temp.innerHTML = `Tempature: <span>${convertion(tempature)}C</span>`
            description.innerHTML = `Sky Conditions:<span>${descrip}</span>`
            wind.innerHTML = `Wind Speed: <span>${wndspd} km/h </span>`
                
        })

        .catch(err => alert('you entered wrong city name'))


    })
