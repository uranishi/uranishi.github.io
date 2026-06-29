import { highlightSearchTerm } from "./highlight-search-term.js";

document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("bibsearch");
  if (!searchInput) {
    return;
  }

  function getPublicationRoots() {
    return document.querySelectorAll("#pub-view-year, #pub-view-category");
  }

  function clearFilterState() {
    getPublicationRoots().forEach((root) => {
      root.querySelectorAll(".unloaded").forEach((element) => {
        element.classList.remove("unloaded");
      });
    });

    if (CSS.highlights) {
      CSS.highlights.delete("search");
    }
  }

  function getActiveBibliographies() {
    const activeView = document.querySelector(".pub-view:not(.d-none):not([hidden])");
    if (activeView) {
      return activeView.querySelectorAll(".bibliography");
    }
    return document.querySelectorAll(".bibliography");
  }

  const filterItems = (searchTerm) => {
    clearFilterState();

    if (!searchTerm) {
      return;
    }

    getActiveBibliographies().forEach((element) => element.classList.remove("unloaded"));

    const selector = ".pub-view:not(.d-none):not([hidden]) .bibliography > li";
    const fallbackSelector = ".bibliography > li";

    if (CSS.highlights) {
      const nonMatchingElements = highlightSearchTerm({
        search: searchTerm,
        selector: document.querySelector(".pub-view") ? selector : fallbackSelector,
      });
      if (nonMatchingElements == null) {
        return;
      }
      nonMatchingElements.forEach((element) => {
        element.classList.add("unloaded");
      });
    } else {
      const items = document.querySelectorAll(document.querySelector(".pub-view") ? selector : fallbackSelector);
      items.forEach((element) => {
        const text = element.innerText.toLowerCase();
        if (text.indexOf(searchTerm) === -1) {
          element.classList.add("unloaded");
        }
      });
    }

    const activeView = document.querySelector(".pub-view:not(.d-none):not([hidden])");
    const headingScope = activeView || document;
    headingScope.querySelectorAll("h2.bibliography").forEach(function (element) {
      let iterator = element.nextElementSibling;
      let hideFirstGroupingElement = true;
      while (iterator && iterator.tagName !== "H2") {
        if (iterator.tagName === "OL") {
          const ol = iterator;
          const unloadedSiblings = ol.querySelectorAll(":scope > li.unloaded");
          const totalSiblings = ol.querySelectorAll(":scope > li");

          if (unloadedSiblings.length === totalSiblings.length) {
            if (ol.previousElementSibling && ol.previousElementSibling.tagName === "H3") {
              ol.previousElementSibling.classList.add("unloaded");
            }
            ol.classList.add("unloaded");
          } else {
            hideFirstGroupingElement = false;
          }
        }
        iterator = iterator.nextElementSibling;
      }
      if (hideFirstGroupingElement) {
        element.classList.add("unloaded");
      }
    });
  };

  const updateInputField = () => {
    filterItems(searchInput.value.toLowerCase().trim());
  };

  let timeoutId;
  searchInput.addEventListener("input", function () {
    clearTimeout(timeoutId);
    const searchTerm = this.value.toLowerCase().trim();
    timeoutId = setTimeout(() => filterItems(searchTerm), 300);
  });

  document.addEventListener("publications-view-changed", updateInputField);

  updateInputField();
});
