
let text_Area = document.getElementById("question");
const click_Button = document.getElementById('click');
click_Button.addEventListener("click", function(event){
    event.preventDefault();
fetch("http://127.0.0.1:5000/analyse?question="+text_Area.value)
    .then(function (response){
            if (response.status !== 200) {
                console.log('Erreur: ' + response.status);
            return;
            }
            response.json().then(publish)
    });

function publish(data) {
    const chat_elt = document.getElementById('chat_box');
    const answer = document.createElement("div");
    /*let elt_to_publish = `<p class="question_right">${text_Area.value}</p>
    <p class="answer_left">Voici l'adresse: ${data.information.address}</p>
    <div id="map" class="answer_left"></div>
    <p class="answer_left">${data.gp_history[0]}<br>${data.gp_history[1]}.<br> Si tu veux en savoir plus,
    va voir sur <a href="${data.gp_history[2]}">Wikipedia</a>.</p>`;*/
    let elt_to_publish = `<p class="question_right">${text_Area.value}</p>
    <p class="answer_left">Voici l'adresse: ${data.information}</p>
    <img id="map" src="../static/image/grandpiCarre.png" alt="Grandpi's logo">
    <p class="answer_left">${data.gp_history[0]}<br>${data.gp_history[1]}.<br> Si tu veux en savoir plus,
    va voir sur <a href="${data.gp_history[2]}">Wikipedia</a>.</p>`;
    answer.innerHTML = elt_to_publish;
    chat_elt.appendChild(answer);
    initMap(data)
    return data;
}
let map;

function initMap(data) {
    console.log(document.getElementById("map"));
    const myLatLng = { lat: data.information.lati, lng: data.information.lngi };
  map = new google.maps.Map(document.getElementById("map"), {
    center: myLatLng,
    zoom: 12,
  });
  console.log(map);
  new google.maps.Marker({
    position: myLatLng,
    map,
      });
}});
