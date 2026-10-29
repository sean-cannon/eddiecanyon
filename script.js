// Skin switcher. The chosen skin is remembered in this browser only.
(function () {
  var KEY = "ec-skin";
  var root = document.documentElement;

  function apply(skin) {
    // Any skin with a button on the page is valid, so new skins need no change here.
    if (!skin || !document.querySelector('[data-skin-btn="' + skin + '"]')) skin = "95";
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
