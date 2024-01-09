// document.addEventListener('DOMContentLoaded', function () {
//     const body = document.body;
//     const toggleDarkModeButton = document.getElementById('toggleDarkMode');

//     // Vérifie l'état initial du mode sombre dans localStorage
//     const isDarkMode = localStorage.getItem('darkMode') === 'enabled';

//     // Applique le mode sombre si nécessaire
//     if (isDarkMode) {
//         body.classList.add('dark-mode');

//         // Ajoutez ici la classe spécifique au mode sombre que vous souhaitez
//     }

//     // Ajoute un écouteur d'événements pour le bouton de bascule
//     toggleDarkModeButton.addEventListener('click', function () {
//         // Bascule entre les classes dark-mode et non-dark-mode
//         body.classList.toggle('dark-mode');

//         // Ajoutez ici la classe spécifique au mode sombre que vous souhaitez
//         if (body.classList.contains('dark-mode')) {
//             localStorage.setItem('darkMode', 'enabled');
//             // Ajoutez ici la classe spécifique au mode sombre que vous souhaitez
//         } else {
//             localStorage.setItem('darkMode', 'disabled');

//             // Retirez ici la classe spécifique au mode sombre si nécessaire
//         }
//     });
// });
