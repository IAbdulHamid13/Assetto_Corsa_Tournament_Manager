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
            box.addEventListener("click", () => {
                if (!container.classList.contains("select-multiple")){
                    deselectAll(selectableBoxes);
                    selectBox(box);
                } else {
                    const currentSelected = container.querySelectorAll("selected");
                    let max = container.dataset.selectMax || -1;
                    if (max > -1 && currentSelected.length >= max){
                        return;
                    }
                    if (box.classList.contains("selected")) {
                        box.classList.remove("selected")
                    } else {
                        selectBox(box);
                    }
                }
                onBoxClick(box);
            });
        });
    })
}

function selectBox(box) {
    box.classList.add("selected");
}

function deselectAll(selectableBoxes) {
    selectableBoxes.forEach(box => {
        box.classList.remove("selected");
    })
}

function setBoxClick(onBoxClickCallback) {
    onBoxClick = onBoxClickCallback;
}

export {setBoxClick};