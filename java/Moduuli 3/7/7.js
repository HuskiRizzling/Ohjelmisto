const hoveri = document.getElementById("trigger");
const targetti = document.getElementById("target");

hoveri.addEventListener("mouseover", function() {
  targetti.src = "img/picB.jpg";
});

hoveri.addEventListener("mouseout", function() {
  targetti.src = "img/picA.jpg";
});

