// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

// Get the header
var header = document.getElementById("myHeader");
var logo = document.getElementById("logo")
var container = document.getElementById("container-case");

// Get the offset position of the navbar
var sticky = header.offsetTop;

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
    logo.classList.add("show");
    container.classList.add("margin")
    
  } else {
    header.classList.remove("sticky");
    logo.classList.remove("show")
    container.classList.remove("margin");
  }
}