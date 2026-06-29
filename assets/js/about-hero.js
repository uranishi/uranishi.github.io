(function () {
  const hero = document.querySelector(".about-hero");
  if (!hero) return;

  const scrollClass = "about-hero-scrolled";
  const threshold = Math.max(hero.offsetHeight - 72, 120);

  function updateNavbar() {
    document.body.classList.toggle(scrollClass, window.scrollY > threshold);
  }

  window.addEventListener("scroll", updateNavbar, { passive: true });
  window.addEventListener("resize", updateNavbar, { passive: true });
  updateNavbar();
})();
