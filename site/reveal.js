// Sections ease up into place as you scroll down to them. Only what starts below the screen is
// animated, so the top of the page never flashes, and with scripts off or Reduce Motion on
// everything is simply there.
document.addEventListener("DOMContentLoaded", function () {
  if (!("IntersectionObserver" in window) || matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  var seen = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      entry.target.classList.remove("below");
      seen.unobserve(entry.target);
    });
  }, { rootMargin: "0px 0px -12% 0px" });
  document.querySelectorAll("[data-reveal]").forEach(function (el) {
    if (el.getBoundingClientRect().top < window.innerHeight * 0.9) return;
    el.classList.add("below");
    seen.observe(el);
  });
});
