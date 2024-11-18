
document.addEventListener('DOMContentLoaded', function() {
  var menuButton = document.getElementById('menu-button');
  var agregarLibroButton = document.getElementById('agregar-libro');
  var formulario = document.getElementById('formulario-agregar-libro');

  if (menuButton) {
    menuButton.addEventListener('click', function() {
      var menu = document.getElementById('dropdown-menu');
      if (menu.style.display === 'block') {
        menu.style.display = 'none';
      } else {
        menu.style.display = 'block';
      }
    });
  }

  if (agregarLibroButton) {
    agregarLibroButton.addEventListener('click', function() {
      if (formulario.style.display === 'block') {
        formulario.style.display = 'none';
      } else {
        formulario.style.display = 'block';
      }
    });
  }

  // Cerrar el menú si se hace clic fuera de él
  window.onclick = function(event) {
    if (!event.target.matches('#menu-button')) {
      var dropdowns = document.getElementsByClassName('caja-menu');
      for (var i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.style.display === 'block') {
          openDropdown.style.display = 'none';
        }
      }
    }
  }
});