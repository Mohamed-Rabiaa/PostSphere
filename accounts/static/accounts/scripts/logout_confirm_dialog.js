document.getElementById('logout-link').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent the default logout action
    const confirmLogout = confirm("Chages are not saved, Are you sure you want to log out?");
    if (confirmLogout) {
        // Redirect the user to the logout view
        window.location.href = '/accounts/logout/';
    }
});
