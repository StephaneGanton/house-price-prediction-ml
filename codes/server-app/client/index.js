function onPageLoad() {
    console.log("document 1oaded");
    var url = "http://127.0.0.1:5000/get_location_names";
    
    $.get(url, function(data, status){

        console.log("got response for get location names request");

        if(data){
            var locations = data.locations;
            //console.log(data);
            //var uilocations = document.getElementById("uiLocations");

            $("#uiLocations").empty();
            for(var i in locations){
                var opt = new Option(locations[i]) ;
                $("#uiLocations").append(opt);
            }
        }
    });  
}   


function getBHKValue(){
    var uiBHK = document.getElementsByName('uiBHK');
    for(var i in uiBHK){
        if(uiBHK[i].checked) return parseInt(i) + 1;
    }

    return -1; //when there is invalid value
}

function getBathValue(){
    var uiBathrooms = document.getElementsByName('uiBathrooms');
    for(var i in uiBathrooms){
        if(uiBathrooms[i].checked) return parseInt(i) + 1;
    }

    return -1; //when there is invalid value
}


function onClickedEstimatePrice(){
   var url = "http://127.0.0.1:5000/predict_home_price";

   var sqft = document.getElementById("uiSqft") 
   var bhk = getBHKValue();
   var bathrooms =  getBathValue();
   var location = document.getElementById("uiLocations");
   var estimatePtrice = document.getElementById("uiEstimatedPrice")

   $.post(url, {
        total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bathrooms,
        location : location.value

    },function (data, status){
        estimatePtrice.innerHTML = "<h2> " + data.estimated_price.toString() + " Lakh</h2>"
        console.log (status);
        console.log(data.estimated_price)
    })
}

window.onload = onPageLoad;