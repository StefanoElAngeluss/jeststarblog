$(document).ready(function() {
  // Ajouter une animation de hover à tous les éléments avec la classe .sticky-note
  $('.sticky-note').hover(function() {
    $(this).addClass('hover');
  }, function() {
    $(this).removeClass('hover');
  });
});

$(document).ready(function() {
  // Obtenir la date actuelle
    // Obtenir la date actuelle
    var currentDate = new Date();

    // Formater la date en utilisant Moment.js
    var formattedDate = moment(currentDate).locale('fr').format('dddd DD MMMM YYYY');

    // Mettre à jour le contenu de l'élément p avec la date formatée
    $('#current-date').text(formattedDate);
  });
