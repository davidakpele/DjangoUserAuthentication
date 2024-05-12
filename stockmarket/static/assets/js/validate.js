const password_input = document.querySelector("#password_input");
const password_eye = document.querySelector("#password_eye");
let loweruppercase = document.querySelector(".loweruppercase i");
let loweruppercasetext = document.querySelector(".loweruppercase span");

let numbercase = document.querySelector(".numbercase i");
let numbercasetext = document.querySelector(".numbercase span");
let specialcase = document.querySelector(".specialcase i");
let specialcasetext = document.querySelector(".specialcase span");

let numcharacter = document.querySelector(".numcharacter i");
let numcharactertext = document.querySelector(".numcharacter span");

password_eye.addEventListener('click',()=>{
if(password_input.type=="password"){
password_input.type="text";
password_eye.classList.add("fa-eye");
password_eye.classList.remove("fa-eye-slash");


}else if(password_input.type=="text"){
password_input.type="password";
password_eye.classList.add("fa-eye-slash");
password_eye.classList.remove("fa-eye");
}

});

// password_input.addEventListener('keyup',function(){
    
//     let pass = document.getElementById("password_input").value;
//     passStrength(pass);
// });

// function passStrength(pass){
   
//     if(pass.match(/([a-z].*[A-Z])|([A-Z].*[a-z])/)){
    
//         loweruppercase.classList.remove("fa-circle");
//         loweruppercase.classList.add("fa-check");
//         loweruppercase.classList.add("green-color");
//         loweruppercasetext.classList.add("green-color");
//     }else{
        
//         loweruppercase.classList.remove("fa-check");
//         loweruppercase.classList.add("fa-circle");
//         loweruppercase.classList.remove("green-color");
//         loweruppercasetext.classList.remove("green-color");
//     }
    
//     if(pass.match(".*\\d.*")){
        
//         numbercase.classList.remove("fa-circle");
//         numbercase.classList.add("fa-check");
//         numbercase.classList.add("green-color");
//         numbercasetext.classList.add("green-color");
//     }else{
        
//         numbercase.classList.remove("fa-check");
//         numbercase.classList.add("fa-circle");
//         numbercase.classList.remove("green-color");
//         numbercasetext.classList.remove("green-color");
//     }
    
    
//     if(pass.match(/[`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/)){
        
//         specialcase.classList.remove("fa-circle");
//         specialcase.classList.add("fa-check");
//         specialcase.classList.add("green-color");
//         specialcasetext.classList.add("green-color");
//     }else{
        
//         specialcase.classList.remove("fa-check");
//         specialcase.classList.add("fa-circle");
//         specialcase.classList.remove("green-color");
//         specialcasetext.classList.remove("green-color");
//     }
    
//     if(pass.length>7){
        
//         numcharacter.classList.remove("fa-circle");
//         numcharacter.classList.add("fa-check");
//         numcharacter.classList.add("green-color");
//         numcharactertext.classList.add("green-color");
//     }else{
        
//         numcharacter.classList.remove("fa-check");
//         numcharacter.classList.add("fa-circle");
//         numcharacter.classList.remove("green-color");
//         numcharactertext.classList.remove("green-color");
//     }
//     if (pass.match(/([a-z].*[A-Z])|([A-Z].*[a-z])/) && pass.match(".*\\d.*") && pass.match(/[`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/) && pass.length>7) {
//         document.getElementById("loginButton").removeAttribute("disabled");
//         document.getElementById("loginButton").classList.remove('inactive');
//         document.getElementById("loginButton").classList.add('active');
//     } else {
//         document.getElementById("loginButton").setAttribute("disabled", "disabled");
//         document.getElementById("loginButton").classList.remove('active');
//         document.getElementById("loginButton").classList.add('inactive');
//     }
    
    
// }


$(document).ready(function () {
    $('#loginButton').click(function (e) {
        e.preventDefault(0)
        let __email = $("input#email").val();
        let __password = $("input#password_input").val();
        if (__email == "") {
            $("#AdminLoginerrorMessage").fadeIn().text("Please enter your username");
            $("input#email").focus();
            return false;
        } 
        if (__password == "") {
            $("#AdminLoginerrorMessage").fadeIn().text("Please enter your password");
            $("input#password_input").focus();
            return false;
        }
        const data = {"email": __email, "password": __password};
        $.ajax({
            type: 'POST', // define the type of HTTP verb we want to use (POST for our form)
            dataType: 'JSON',
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(data), // our data object
            url: '/auth/login',
            processData: false,
            encode: true,
            crossOrigin: true,
            async: true,
            crossDomain: true,
            headers: {
                'Access-Control-Allow-Methods': '*',
                "Access-Control-Allow-Credentials": true,
                "Access-Control-Allow-Headers": "Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization",
                "Access-Control-Allow-Origin": "*",
                "Control-Allow-Origin": "*",
                "cache-control": "no-cache",
                'Content-Type': 'application/json'
            },
        }).then((response) => { 
            //user is logged in successfully in the back-end
            if (response.status == 200) {
                setTimeout(function () {
                    window.location.reload(1);
                }, 0);
            } else {
                $("#AdminLoginerrorMessage").fadeIn(response.message);
            }
        }).fail((xhr, error) => {
            $("#AdminLoginerrorMessage").fadeIn().text(error,'Oops...Server is down! error', xhr);
        });
    })
});
