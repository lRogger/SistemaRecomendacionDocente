
 // Mostrar y ocultar el menú al hacer clic en el botón
 document
 .getElementById("user-menu-button")
 .addEventListener("click", function (event) {
   event.stopPropagation(); // Evita que el clic se propague al documento
   const menu = event.currentTarget.nextElementSibling;
   const isVisible = menu.classList.contains("hidden");
   if (isVisible) {
     menu.classList.remove("hidden");
   } else {
     menu.classList.add("hidden");
   }
 });

// SIDBAR

// document.getElementsBy
document
 .getElementById("btn-close-sidebar")
 .addEventListener("click", function (event) {
   const sideBarMenu = document.getElementById("hidden-sidebar-movil");
   const sideBarMenuBackground = document.getElementById(
     "hidden-sidebar-background-movil"
   );

   sideBarMenuBackground.classList.add("hidden");
   sideBarMenu.classList.add("hidden");
 });

document
 .getElementById("btn-open-sidebar")
 .addEventListener("click", function (event) {
   const sideBarMenu = document.getElementById("hidden-sidebar-movil");
   const sideBarMenuBackground = document.getElementById(
     "hidden-sidebar-background-movil"
   );

   sideBarMenuBackground.classList.remove("hidden");
   sideBarMenu.classList.remove("hidden");
 });

// Cerrar el menú si el usuario hace clic fuera
document.addEventListener("click", function (event) {
 const menu = document.querySelector(".dropdown-menu");
 const button = document.getElementById("user-menu-button");
 if (menu && !menu.contains(event.target) && event.target !== button) {
   menu.classList.add("hidden");
 }
});