(function () {
  function openSectionForHash() {
    var hash = window.location.hash;
    if (!hash) {
      return;
    }
    var target = document.querySelector(hash);
    if (!target) {
      return;
    }
    var section = target.closest(".cv-section-card");
    if (section) {
      section.open = true;
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".cv-jump-nav__link").forEach(function (link) {
      link.addEventListener("click", function () {
        var target = document.querySelector(link.getAttribute("href"));
        if (target) {
          var section = target.closest(".cv-section-card");
          if (section) {
            section.open = true;
          }
        }
      });
    });

    openSectionForHash();
  });

  window.addEventListener("hashchange", openSectionForHash);
})();
