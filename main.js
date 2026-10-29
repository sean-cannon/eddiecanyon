// Highlight the rail link for the section on screen.
(function () {
  var links = document.querySelectorAll(".rail a[data-sec]");
  if (!("IntersectionObserver" in window) || !links.length) return;

  var byId = {};
  links.forEach(function (a) { byId[a.getAttribute("data-sec")] = a; });

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      links.forEach(function (a) { a.classList.remove("on"); });
      var a = byId[e.target.id];
      if (a) a.classList.add("on");
    });
  }, { rootMargin: "-45% 0px -50% 0px" });

  Object.keys(byId).forEach(function (id) {
    var el = document.getElementById(id);
    if (el) io.observe(el);
  });
})();
