const navBar = document.getElementsByClassName("nav-bar");
const removeButton = document.getElementById("remove-nav");
const showButton = document.getElementById("show-nav");

showButton.addEventListener("click", ()=>{
    localStorage.clear()
    navBar[0].style.display = "flex";
    
});

removeButton.addEventListener("click", ()=>{
    navBar[0].style.display = "none";
    localStorage.setItem("remove-navbar", "none");
});

if (localStorage.length > 0){
    navBar[0].style.display = localStorage.getItem("remove-navbar")
};