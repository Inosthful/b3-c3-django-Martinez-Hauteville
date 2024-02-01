
$(document).ready(function() {
    // Fonction pour obtenir l'état actuel du mode
   
    function getDarkMode() {
        
        $.get('/dark-mode/', function(data) {
            const darkmodeButton = document.getElementById("toggleDarkMode")
            if (data.dark_mode) {
                document.body.setAttribute("data-theme", "dark")
                darkmodeButton.innerHTML = "Dark Mode: ON"
                console.log("mode sombre")
            } else {
                document.body.setAttribute("data-theme", "light")
                darkmodeButton.innerHTML = "Dark Mode: OFF"
                console.log("mode clair")
            }
        });
    }

    // Appeler la fonction pour activer le mode lors du chargement de la page
       getDarkMode();

    $('#toggleDarkMode').click(function() {
        $.post('/dark-mode/', function(data) {
            if (data.status === 'success') {
                // Appeler à nouveau la fonction pour basculer entre les modes
                getDarkMode();
            }
        });
    });
});
