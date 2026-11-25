import {setBoxClick} from "./selectable_item_box.js";
import {FilterSortCollection} from "./FilterSortCollection.js";

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

    const testItemBoxes = document.querySelectorAll(".test-item-box");
    testItemBoxes.forEach(box => {
        let rgbStr = "rgb(";
        for (let i = 0; i < 3; i++) {
            const val = Math.round(Math.random() * 255);
            rgbStr += val;
            if (i < 2) {
                rgbStr += ", ";
            }
        }
        rgbStr += ")"
        box.style.backgroundColor = rgbStr;
    })

    initDynamicCheckboxes();
    initFilterSorts();
}

function initFilterSorts() {
    const trackFilterSort = new FilterSortCollection("tracks-container", ".item-box");
    trackFilterSort.setItemData(trackBox => {
        const trackName = trackBox.querySelector(".item-name");
        if (trackName) return trackName.innerText;
        return "";
    });
    trackFilterSort.setupSearch("tracks-search");
    trackFilterSort.addSort("name", 1)
    const trackSortName = document.getElementById("track-sort-name");
    if (trackSortName) {
        trackSortName.addEventListener("click", trackFilterSort.sortEvent("name", trackFilterSort));
    }
    const carFilterSort = new FilterSortCollection("cars-container", ".item-box");
    carFilterSort.setItemData(carBox => {
        const carName = carBox.querySelector(".item-name");
        if (carName) return carName.innerText;
        return "";
    })
    carFilterSort.setupSearch("cars-search");
    const carSortName = document.getElementById("car-sort-name");
    if (carSortName) {
        carSortName.addEventListener("click", carFilterSort.sortEvent("default", carFilterSort));
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

function initDynamicCheckboxes() {
    const dynamicCheckboxes = document.querySelectorAll("input[type='checkbox']");
    dynamicCheckboxes.forEach(checkbox => {
        checkbox.addEventListener("change", checkboxToggle(checkbox));
        updateCheckbox(checkbox);
    })
}

function checkboxToggle(checkbox) {
    return function() {
        updateCheckbox(checkbox)
    }
}

function updateCheckbox(checkbox) {
    const element = document.getElementById(checkbox.dataset.target);
    if (element) {
        const inputs = element.querySelectorAll("input");
        if (checkbox.checked) {
            element.style.visibility = "visible";
            inputs.forEach(input => {
                input.removeAttribute("disabled");
            })
        } else {
            element.style.visibility = "hidden";
            inputs.forEach(input => {
                input.setAttribute("disabled", "");
            })
        }
    }
}