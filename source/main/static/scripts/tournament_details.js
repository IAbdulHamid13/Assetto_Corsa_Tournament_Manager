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
        const tournamentEvents = document.getElementById("tournament-events");
        if (tournamentEvents) {
            tournamentEvents.scroll({"left": tournamentEvents.scrollWidth / 2, "behavior": "smooth"});
        }
    }
}

function scrollToDetails() {
    if (detailsOpen) {
        const tournamentEvents = document.getElementById("tournament-events");
        if (tournamentEvents) {
            tournamentEvents.scroll({"left": tournamentEvents.scrollWidth / 2, "behavior": "smooth"});
        }
    }
}