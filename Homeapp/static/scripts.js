
    function showMenu(menuId) {
        // Hide both menus first
        document.getElementById('veg-menu').style.display = "none";
        document.getElementById('nonveg-menu').style.display = "none";
      
        // Show the selected menu
        document.getElementById(menuId).style.display = "flex";
        document.getElementById(menuId).scrollIntoView({ behavior: 'smooth' });
    }
