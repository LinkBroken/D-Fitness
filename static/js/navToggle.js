const navBar = document.getElementsByClassName("nav-bar");
const showButton = document.getElementById("show-nav");

if(localStorage.length != 0){
    navBar[0].style.display = localStorage.getItem("nav-hide")
};
showButton.addEventListener("click", ()=>{
    localStorage.setItem("nav-hide", "none");
    if (navBar[0].style.display == "none"){
        navBar[0].style.display = "flex";
        localStorage.clear()
    
    }
    else {
        navBar[0].style.display = "none";
        
    }

});

