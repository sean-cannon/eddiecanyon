// Rail highlight, id10t photo reveal, and the color palette picker.
(function () {
  // --- palette ---
  var KEY = "ec-palette";
  var root = document.documentElement;
  var meta = document.querySelector('meta[name="theme-color"]');

  function applyPalette(name) {
    if (!name || !document.querySelector('[data-palette-btn="' + name + '"]')) name = "acid";
    if (name === "acid") root.removeAttribute("data-palette");
    else root.setAttribute("data-palette", name);
    document.querySelectorAll("[data-palette-btn]").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.getAttribute("data-palette-btn") === name));
    });
    if (meta) meta.setAttribute("content", getComputedStyle(root).getPropertyValue("--acid").trim());
  }
  applyPalette(root.getAttribute("data-palette") || "acid");

  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-palette-btn]");
    if (!b) return;
    var name = b.getAttribute("data-palette-btn");
    applyPalette(name);
    try { localStorage.setItem(KEY, name); } catch (_) {}
  });

  // --- id10t photo: hover on desktop, tap or Enter to toggle ---
  var collage = document.querySelector(".collage");
  if (collage) {
    var toggle = function () { collage.classList.toggle("reveal"); };
    collage.addEventListener("click", toggle);
    collage.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); toggle(); }
    });
  }

  // --- rail highlight ---
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
