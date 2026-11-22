document.addEventListener("DOMContentLoaded", initTabs);
let tabs;
function initTabs() {
    tabs = document.querySelectorAll(".tabs .tab");
    tabs.forEach(tab => {
        tab.addEventListener("click", onTabClick(tab));
    });
    if (tabs[0]) {
        setTabActive(tabs[0]);
    }
}

function onTabClick(tab) {
    return function() {
        console.log("tab click");
        setTabActive(tab);
    }
}

function setTabActive(tab) {
    const tabContents = document.querySelectorAll(".tab-content");
    tabs.forEach(tab => {
        tab.classList.remove("active");
    })
    tab.classList.add("active");
    tabContents.forEach(tabContent => {
        tabContent.style.display = "none";
    });
    const focusedTab = document.getElementById(tab.dataset.target);
    if (focusedTab) {
        focusedTab.style.display = null;
    }
}