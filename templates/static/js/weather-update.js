// const api = "e6ed093031474d538f6101732240905";

$(document).ready(() => {
  $("#updateLocation").click(() => {
    let addressInp = document.getElementById("id_address");
    function getLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
      } else {
        alert("Browser Not Support Geolocation");
      }
    }
    function showPosition(position) {
      const lat = position.coords.latitude;
      const long = position.coords.longitude;
      getApiLocation(lat, long);
    }
    async function getApiLocation(lat, long) {
      let address = await fetch(
        `http://api.weatherapi.com/v1/current.json?key=e6ed093031474d538f6101732240905&q=${lat}, ${long}&aqi=yes`
      ).then((response) => {
        return response.json();
      });
      console.log(addressInp);
      addressInp.value = `${address.location.name} ${address.location.region} ${address.location.country}`;
    }

    getLocation();
  });
});
