document.addEventListener("DOMContentLoaded", function () {
    // Sidebar Toggle Logic
    const sidebarToggle = document.getElementById("sidebarToggle");
    const sidebar = document.querySelector(".sidebar");
    const content = document.querySelector(".content");

    if (sidebarToggle && sidebar && content) {
        sidebarToggle.addEventListener("click", function () {
            sidebar.classList.toggle("hidden");
            content.classList.toggle("expanded");
        });
    }

    // Tooltips Initialization (Bootstrap)
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Handle Dynamic Book Cover Loading Errors
    document.querySelectorAll(".book-cover").forEach((img) => {
        img.onerror = function () {
            this.src = "/static/img/placeholder.png"; // Fallback image
        };
    });

    // Smooth Scroll for Sidebar Links
    document.querySelectorAll(".sidebar a").forEach((link) => {
        link.addEventListener("click", function (event) {
            event.preventDefault();
            const targetId = this.getAttribute("href").substring(1);
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                window.scrollTo({
                    top: targetSection.offsetTop - 70,
                    behavior: "smooth",
                });
            }
        });
    });
});
