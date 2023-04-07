// alert("Bonjour, je suis le script.js");

// Fonction de changement de l'icone du dropdown
var dropdown1 = document.querySelector('.toggle1');
dropdown1.addEventListener('click', function() {
  var icon = this.querySelector('i');
  if (icon.classList.contains('fa-plus-circle')) {
    icon.classList.remove('fa-plus-circle');
    icon.classList.add('fa-minus-circle');
  } else {
    icon.classList.remove('fa-minus-circle');
    icon.classList.add('fa-plus-circle');
  }
});

dropdown1.addEventListener('blur', function() {
  var icon = this.querySelector('i');
  icon.classList.remove('fa-minus-circle');
  icon.classList.add('fa-plus-circle');
});


var dropdown2 = document.querySelector('.toggle2');
dropdown2.addEventListener('click', function() {
  var icon = this.querySelector('i');
  if (icon.classList.contains('fa-plus-circle')) {
    icon.classList.remove('fa-plus-circle');
    icon.classList.add('fa-minus-circle');
  } else {
    icon.classList.remove('fa-minus-circle');
    icon.classList.add('fa-plus-circle');
  }
});

dropdown2.addEventListener('blur', function() {
  var icon = this.querySelector('i');
  icon.classList.remove('fa-minus-circle');
  icon.classList.add('fa-plus-circle');
});
