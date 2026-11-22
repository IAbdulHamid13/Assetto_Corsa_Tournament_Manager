document.addEventListener("DOMContentLoaded", initEventDetails);
let eventsList;
let eventDetails;
let events;
let detailEventName;

function initEventDetails() {
    events = document.querySelectorAll(".event");
    events.forEach(event => {
        event.addEventListener("click", openEventDetails(event.dataset.query))
    })
    eventsList = document.getElementById("events-list");
    eventDetails = document.getElementById("event-details");
    detailEventName = document.getElementById("detail-event-name");
    if (detailEventName) {
        detailEventName.addEventListener("click", closeEventDetails);
    }
}

function openEventDetails(eventURL = null) {
    return function() {
        // TODO: Perform a fetch on eventURL to get the actual event details
        // fetch(eventURL)...
        if (eventsList) {
            eventsList.style.left = "-100%";
        }
        if (eventDetails) {
            eventDetails.style.left = "-100%";
        }
    }
}

function closeEventDetails() {
    if (eventsList) {
        eventsList.style.left = null;
    }
    if (eventDetails) {
        eventDetails.style.left = null;
    }
}