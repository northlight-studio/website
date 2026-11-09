// The light/dark switch. With no choice saved, the site follows the system setting. This runs in
// the <head>, before the page paints, so a saved choice never flashes the other theme first.
(function () {
  var root = document.documentElement;
  var saved = null;
  try { saved = localStorage.getItem("theme"); } catch (e) {}
  if (saved === "light" || saved === "dark") root.setAttribute("data-theme", saved);
  root.classList.add("js");

  function current() {
    return root.getAttribute("data-theme") || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  }

  document.addEventListener("DOMContentLoaded", function () {
    var button = document.querySelector(".theme");
    if (!button) return;
    button.addEventListener("click", function () {
      var next = current() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) {}
    });
  });
})();
