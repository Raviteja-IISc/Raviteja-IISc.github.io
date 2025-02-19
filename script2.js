// Function to show the selected tab and hide the others
function showTab(tabName) {
    var sections = document.querySelectorAll(".project-section");
    sections.forEach(section => section.style.display = "none"); // Hide all sections

    document.getElementById(tabName).style.display = "block"; // Show selected tab
}

// Function to toggle 'View More' / 'View Less' for additional projects
function toggleViewMore(id, buttonId) {
    var moreProjects = document.getElementById(id);
    var button = document.getElementById(buttonId);

    // Toggle the display of additional projects
    if (moreProjects.style.display === "none" || moreProjects.style.display === "") {
        moreProjects.style.display = "grid"; // Show the extra projects
        button.textContent = "View Less";  // Change button text to 'View Less'
    } else {
        moreProjects.style.display = "none"; // Hide the extra projects
        button.textContent = "View More";  // Change button text back to 'View More'
    }
}

// Ensure the correct tab is displayed by default when the page loads
window.onload = function() {
    showTab('ml');  // Show 'Machine Learning' tab by default
};
