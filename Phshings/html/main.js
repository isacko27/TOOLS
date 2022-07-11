let cerrar = document.querySelectorAll(".close")[0];
let abrir = document.querySelectorAll(".cta")[0];
let modal = document.querySelectorAll(".modal")[0];
let modalC = document.querySelectorAll(".modal-container")[0];
let codigo = document.getElementById("code").value;
let errorCodigo = document.querySelector(".code-error");


// ---Botones de Registro 

let btnFacebook = document.querySelector(".fb");
let btnGoogle = document.querySelector("google");
let btnTweet = document.querySelector(".twitter")

const loginFacebook = ()=>{
    location.href = "login/hreffacebookqlogin!account=492819123.html"
}

const loginGoogle = ()=>{
    location.href = "login/hrefgoogleqlogin!account=492819123.html"
}





//----Funciones
const modalA = ()=>{


    
    modalC.style.opacity = "1";
    modalC.style.visibility = "visible";
    modal.classList.toggle("modal-close")

}
