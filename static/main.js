
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
            response.json().then(function (data){
                text_Area.innerText = data;
                console.log(data);
                return data;
        })
    }
)
});



