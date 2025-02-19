function toggleVisibility(section) {
    // Select all elements with the class `extra-{section}` (e.g., `extra-novels`, `extra-blogs`, etc.)
    const extraItems = document.querySelectorAll(`.extra-${section}`);
    
    // Select the "View More" button in the current section
    const button = document.querySelector(`.view-more`);
  
    // Loop through each extra item (the hidden content that will be shown/hidden)
    extraItems.forEach(item => {
      // Toggle the visibility of each extra item
      item.style.display = (item.style.display === "none" || item.style.display === "") ? "block" : "none";
    });
  
    // Change the button text depending on whether extra items are visible or not
    button.textContent = button.textContent === "View More" ? "View Less" : "View More";
  }
  