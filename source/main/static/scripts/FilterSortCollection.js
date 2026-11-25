class FilterSortCollection {
    #collectionContainer; // The container of your collectionItems, needed to reorder the collectionItems within them
    #collectionItems; // The objects you want to show, hide, reorder
    #itemData; // A callable that accepts a collectionItem and uses it to return a string that is the data to be used for filtering and sorting
    #filters; // A collection of callables that accept a collectionItem and returns true if it should be shown and false if it should not
    #sorts;
    #currentSort;


    /* FILTERING */
    constructor(collectionContainerID, collectionItemSelector, itemDataCallable = null, filters = null, sorts = null) {
        this.setCollectionContainer(collectionContainerID);
        this.setCollectionItems(collectionItemSelector);
        this.setSorts(sorts);
        this.setItemData(itemDataCallable);
        this.setFilters(filters);
        this.#currentSort = {
            name: "none",
            order: 0 // 1 for ascending, -1 for descending
        }
    }

    setCollectionContainer(collectionContainerID) {
        this.#collectionContainer = document.getElementById(collectionContainerID);
    }

    setCollectionItems(collectionItemSelectorRelativeToContainer) {
        if (!this.#collectionContainer) throw new Error("Need a container to find the collection items");
        const nodeList = document.querySelectorAll(`#${this.#collectionContainer.id} > ${collectionItemSelectorRelativeToContainer}`);
        this.#collectionItems = Array.from(nodeList);

    }

    setItemData(itemDataCallable) {
        if (itemDataCallable) this.#itemData = itemDataCallable
        else this.#itemData = collectionItem => {
            collectionItem.innerText;
        }
        // Add a default sort
        this.addSort("default", 1, itemDataCallable);
    }

    setFilters(filters) {
        if (filters) this.#filters = filters
        else this.#filters = [];
    }

    addFilter(filter) {
        this.#filters.push(filter);
    }

    applyFilters(instance = this) {
        for (const collectionItem of instance.#collectionItems) {
            let show = false;
            for (const filter of instance.#filters) {
                if (filter(collectionItem)) {
                    show = true;
                    break;
                }
            }
            if (show) {
                collectionItem.style.display = null; // collectionItems must have some visible display by default
            } else {
                collectionItem.style.display = "none";
            }
        }
    }

    #applyFiltersHandler(instance) {
        return function() {
            instance.applyFilters(instance);
        }
    }

    setupSearch(searchInputID) {
        const searchInput = document.getElementById(searchInputID);
        if (searchInput) {
            this.addFilter(collectionItem => {
                if (this.#itemData(collectionItem) === "") return true; // If we can't actually search on this item, show it anyway.
                return this.#itemData(collectionItem).toLowerCase().includes(searchInput.value);
            })
            searchInput.addEventListener("input", this.#applyFiltersHandler(this));
        }
    }

    /* SORTING */
    setSorts(sorts) {
        if (sorts) this.#sorts = sorts
        else this.#sorts = {};
    }

    addSort(name, sortType, itemDataCallable = null) {
        if (!itemDataCallable) itemDataCallable = this.#itemData;
        if (sortType === 1) {// Alphabetical
            this.#sorts[name] = (itemA, itemB) => itemDataCallable(itemA).localeCompare(itemDataCallable(itemB));
        } else if (sortType === 2) { // Numerical
            this.#sorts[name] = itemDataCallable(parseFloat(itemA)) - itemDataCallable(parseFload(itemB));
        }
    }

    sort(name, instance = this) {
        if (!instance.#collectionItems) throw new Error("No collection items to sort.");
        if (!instance.#collectionContainer) throw new Error("No collection container for items.");
        if (!instance.#sorts.hasOwnProperty(name)) throw new Error(`No sort for ${name} set up.`);
        if (instance.#currentSort.name === name) {
            instance.#currentSort.order *= -1; // Flip if we do the same sort more than once
        } else {
            instance.#currentSort = {
                name: name,
                order: 1
            };
        }
        instance.#collectionItems.sort((itemA, itemB) => instance.#sorts[name](itemA, itemB) * instance.#currentSort.order);
        instance.#collectionItems.forEach(item => {
            instance.#collectionContainer.appendChild(item);
        });
    }

    sortEvent(name, instance) {
        return function() {
            instance.sort(name, instance);
        }
    }
}


export {FilterSortCollection};