document.addEventListener("DOMContentLoaded", initEventDetails);
let detailsOpen = false;

function initEventDetails() {
    const events = document.querySelectorAll(".event");
    events.forEach(event => {
        event.addEventListener("click", openEventDetails(event.dataset.query))
    })
}

function openEventDetails(eventURL = null) {
    return function() {
        detailsOpen = true;
        // TODO: Perform a fetch on eventURL to get the actual event details
        // fetch(eventURL)...
        const eventsList = document.getElementById("events-list");
        if (eventsList) {
            eventsList.style.left = "-100%";
        }
        const eventDetails = document.getElementById("event-details");
        if (eventDetails) {
            eventDetails.style.left = "-100%";
        }
    }
}