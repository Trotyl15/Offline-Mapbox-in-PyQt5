var map ;
$(function () {
    myMap()
    $('body').click(function () {
        alert("123")
        addMarker(48.5107057+1*Math.random(), -71.65168481*Math.random(),map)
    })
    function myMap() {
        var mapProp = {
            center: new google.maps.LatLng(48.5107057, -71.6516848),
            zoom: 15,
            mapTypeId: google.maps.MapTypeId.SATELLITE
        };
    
    
        map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
    }
    function addMarker(location, map) {
        var marker = new google.maps.Marker({
            position: location,
            title: 'Home Center',
            map:map
        });
    }
})

