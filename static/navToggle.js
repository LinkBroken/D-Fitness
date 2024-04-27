const navBar = document.getElementsByClassName("nav-bar");
const removeButton = document.getElementById("remove-nav");
const showButton = document.getElementById("show-nav");
showButton.style.display= "none";

showButton.addEventListener("click", ()=>{
    localStorage.clear();
    showButton.style.display = "none";
    removeButton.style.display = "block";
    navBar[0].style.display = "flex";
    
});

removeButton.addEventListener("click", ()=>{
    navBar[0].style.display = "none";
    removeButton.style.display = "none";
    showButton.style.display = "block";
    localStorage.setItem("remove-navbar", "none");
});

if (localStorage.length > 0){
    navBar[0].style.display = localStorage.getItem("remove-navbar");
};
