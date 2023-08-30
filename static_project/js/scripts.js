
//if current page is login/home page
if (window.location.pathname == "/") {
  // Featured recipe slider
  let slideIndex = 0;


  function showSlides() {
    const slides = document.querySelectorAll(".slider");
    console.log(slides.length)

    for(let i=0; i< slides.length; i++) {
        slides[i].style.display = "none";
    }

    slideIndex++;

    if(slideIndex > slides.length ) {
        slideIndex = 1;
    }



    slides[slideIndex - 1].style.display = "block";


    setTimeout(showSlides, 5000);
  }


  showSlides();

  // toggle eye show password
  const password = document.querySelector('.password-toggle');
  const toggleEye = document.querySelector('.toggle-eye-crossed');

  function showHidePassword() {
    if(password.type === 'password'){
        password.setAttribute('type', 'text');
        toggleEye.classList.add('hide');
        toggleEye.classList.remove('toggle-eye-crossed');
        toggleEye.classList.add('toggle-eye');
    }
    else {
        password.setAttribute('type', 'password');
        toggleEye.classList.add('show');
        toggleEye.classList.remove('toggle-eye');
        toggleEye.classList.add('toggle-eye-crossed');
    }
  }

  toggleEye.addEventListener('click', showHidePassword);
}


// get current year (footer)
const currentDate = new Date;
const year = document.getElementById('year');
year.innerHTML = currentDate.getFullYear();


//Show hide categories 
const catModal = document.querySelector('.categories-modal')
//const catBtns = document.querySelectorAll('.categories-btn')
const catBtn1 = document.querySelector('.categories-btn1')
const catBtn2 = document.querySelector('.categories-btn2')


catBtn1.addEventListener('click', function(){
  catModal.classList.toggle("slide-modal");
})

catBtn2.addEventListener('click', function(){
    catModal.classList.add("slide-modal");
    navbarMobile.classList.remove('show-navbar-mobile');
  })

// catBtns.forEach(function(btn){
//     btn.addEventListener('click', function(){
//         catModal.classList.toggle("slide-modal");
//         navbarMobile.classList.toggle('hide-navbar-mobile');
//     })
// })



// mobile nav
const mobileBtn = document.querySelector('.mobile-menu');
const navbarMobile = document.querySelector('.navbar-mobile');

function showSideNavbar() {
    //if cat modal does not exist toggle navbar mobile
    if (!catModal.classList.contains("slide-modal")){
      navbarMobile.classList.toggle('show-navbar-mobile');
    //if categories modal exists show navbar mobile & hide categories modal
    } else if (catModal.classList.contains("slide-modal")){
      navbarMobile.classList.add('show-navbar-mobile');
      catModal.classList.remove("slide-modal")
    //default
    } else {
      catModal.classList.remove("slide-modal");
      navbarMobile.classList.toggle('show-navbar-mobile');
    }

}

mobileBtn.addEventListener('click', showSideNavbar)

//if window width >= 960px hide navbar mobile
window.addEventListener("resize", function() {
  var newWidth = window.innerWidth;
  if (newWidth >= "960"){
    navbarMobile.classList.remove('show-navbar-mobile');
  }
});



// REGISTER FORM
// const firstname = document.getElementById('firstname');
// const lastname = document.getElementById('lastname');
// const username = document.getElementById('username');
// const email = document.getElementById('email');
// const password1 = document.getElementById('password1');
// const password2 = document.getElementById('password2');
// const registerForm = document.getElementById('register-main-form');
// const error = document.getElementById('error');
// const errors = document.querySelectorAll('#error')




// function processFormData(e){

//     let errorMessages = [];
    
//     //Validate Form
//     if(firstname.value == "" || firstname.value == null){
//         errorMessages.push('first name is required');
//         firstname.style.border = "2px solid tomato";
//     } else {
//       firstname.style.border = "2px solid #ffffff";
//       errorMessages.push('');
//     }

//     if (lastname.value == "" || lastname.value == null) {
//       errorMessages.push('last name is required');
//       lastname.style.border = "2px solid tomato";
//     } else {
//       lastname.style.border = "2px solid #ffffff";
//       errorMessages.push('');
//     }

//     if (username.value == "" || username.value == null) {
//       errorMessages.push('username is required');
//       username.style.border = "2px solid tomato";
//     } else {
//       username.style.border = "2px solid #ffffff";
//       errorMessages.push('');
//     }

//     if (email.value == "" || email.value == null) {
//       errorMessages.push('email is required');
//       email.style.border = "2px solid tomato";
//     } else {
//       email.style.border = "2px solid #ffffff";
//       errorMessages.push('');
//     }

//     if (password1.value == "" || password1.value == null) {
//       errorMessages.push('password is required');
//       password1.style.border = "2px solid tomato";
//     } else {
//       password1.style.border = "2px solid #ffffff";
//       errorMessages.push('');
//     }

//     if (password2.value == "" || password2.value == null) {
//       errorMessages.push('confirm password is required');
//       password2.style.border = "2px solid tomato";
//     } else {
//       password2.style.border = "2px solid #ffffff";
//       errorMessages.push('');
//     }

  

//     // if messages array length has an item
//     if(errorMessages.length > 0) {
//         e.preventDefault();
//         // error.innerText = errorMessages.join('\n')
//         // inputs.forEach(function(input){
//         //   if (input.value !== "" || input.value == null) {
            
//         //   }
//         // });
      
//         errors.forEach(function(item, index){
//           item.innerText = errorMessages[index];
//         })
      
//     }

// }

// // Event Listener
// registerForm.addEventListener('submit', processFormData);



