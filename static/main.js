
let texte_Area = document.getElementById("question");
const click_Button = document.getElementById("click");
click_Button.addEventListener("click", function(){
    console.log("This is ok.")
    let request = new XMLHttpRequest();
        request.open("GET", "http://127.0.0.1:5000/analyse/ ");
        request.send(texte_Area);
});