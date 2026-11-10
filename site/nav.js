// On a narrow screen the tabs scroll sideways. This brings the current page's tab into view, so
// you can always see where you are. With scripts off the tabs still scroll by hand.
document.addEventListener("DOMContentLoaded", function () {
  var tabs = document.querySelector(".tabs");
  var here = tabs && tabs.querySelector('[aria-current="page"]');
  if (!here || tabs.scrollWidth <= tabs.clientWidth) return;
  tabs.scrollLeft = here.offsetLeft - (tabs.clientWidth - here.offsetWidth) / 2;
});
