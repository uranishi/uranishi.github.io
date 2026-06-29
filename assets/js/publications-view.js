(function () {
  var STORAGE_KEY = "publications-view";

  function isValidView(view) {
    return view === "year" || view === "category";
  }

  function setActiveView(view) {
    if (!isValidView(view)) {
      view = "year";
    }

    var yearPanel = document.getElementById("pub-view-year");
    var categoryPanel = document.getElementById("pub-view-category");
    var tabs = document.querySelectorAll(".pub-sort-toggle [data-pub-view]");

    if (yearPanel) {
      var showYear = view === "year";
      yearPanel.classList.toggle("d-none", !showYear);
      yearPanel.hidden = !showYear;
    }

    if (categoryPanel) {
      var showCategory = view === "category";
      categoryPanel.classList.toggle("d-none", !showCategory);
      categoryPanel.hidden = !showCategory;
    }

    for (var i = 0; i < tabs.length; i++) {
      var tab = tabs[i];
      var isActive = tab.getAttribute("data-pub-view") === view;
      tab.classList.toggle("active", isActive);
      tab.setAttribute("aria-selected", isActive ? "true" : "false");
    }

    try {
      localStorage.setItem(STORAGE_KEY, view);
    } catch (e) {
      // ignore storage errors
    }

    document.dispatchEvent(new CustomEvent("publications-view-changed", { detail: { view: view } }));
  }

  document.addEventListener("DOMContentLoaded", function () {
    var toggle = document.querySelector(".pub-sort-toggle");
    if (!toggle) {
      return;
    }

    var initialView = "year";
    try {
      var stored = localStorage.getItem(STORAGE_KEY);
      if (stored && isValidView(stored)) {
        initialView = stored;
      }
    } catch (e) {
      // ignore storage errors
    }

    setActiveView(initialView);

    toggle.addEventListener("click", function (event) {
      var button = event.target.closest("[data-pub-view]");
      if (!button) {
        return;
      }
      setActiveView(button.getAttribute("data-pub-view"));
    });
  });
})();
