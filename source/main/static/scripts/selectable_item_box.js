let selectableContainers;
let onBoxClick = (box) => {
    ;
}
document.addEventListener("DOMContentLoaded", initSelectables);

function initSelectables() {
    selectableContainers = document.querySelectorAll(".selectable-container");
    selectableContainers.forEach(container => {
        const selectableBoxes = container.querySelectorAll(".selectable.item-box");
        selectableBoxes.forEach(box => {
            box.addEventListener("click", selectBox(box, selectableBoxes))
        });
    })
}

function selectBox(box, selectableBoxes) {
    return function() {
        selectableBoxes.forEach(box => {
            box.classList.remove("selected");
        })
        onBoxClick(box);
        box.classList.add("selected");
    }
}

function setBoxClick(onBoxClickCallback) {
    onBoxClick = onBoxClickCallback;
}

export {setBoxClick};