// Skin switcher. The chosen skin is remembered in this browser only.
(function () {
  var KEY = "ec-skin";
  var SKINS = ["95", "geo", "bbs", "mac", "y2k"];
  var root = document.documentElement;

  function apply(skin) {
    if (SKINS.indexOf(skin) < 0) skin = "95";
    root.setAttribute("data-skin", skin);
    var buttons = document.querySelectorAll("[data-skin-btn]");
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].setAttribute("aria-pressed", String(buttons[i].getAttribute("data-skin-btn") === skin));
    }
  }

  apply(root.getAttribute("data-skin") || "95");

  document.addEventListener("click", function (e) {
    var btn = e.target.closest("[data-skin-btn]");
    if (!btn) return;
    var skin = btn.getAttribute("data-skin-btn");
    apply(skin);
    try { localStorage.setItem(KEY, skin); } catch (_) {}
  });
})();
