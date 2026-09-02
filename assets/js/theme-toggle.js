(function () {
  var root = document.documentElement;
  var btn = document.getElementById('theme-toggle');
  if (!btn) return;

  function getStoredTheme() {
    try { return localStorage.getItem('theme'); } catch (e) { return null; }
  }

  function currentTheme() {
    return root.getAttribute('data-theme') ||
      getStoredTheme() ||
      (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  }

  function applyTheme(next) {
    root.setAttribute('data-theme', next);
    btn.setAttribute('aria-pressed', String(next === 'dark'));
    try { localStorage.setItem('theme', next); } catch (e) {}
  }

  // Synchronize button state on load with the active theme
  var active = currentTheme();
  root.setAttribute('data-theme', active);
  btn.setAttribute('aria-pressed', String(active === 'dark'));

  btn.addEventListener('click', function () {
    var next = currentTheme() === 'dark' ? 'light' : 'dark';

    if (!document.startViewTransition) {
      applyTheme(next);
      return;
    }

    root.classList.add('theme-switch');
    var vt = document.startViewTransition(function () {
      applyTheme(next);
    });

    vt.finished.then(
      function () { root.classList.remove('theme-switch'); },
      function () { root.classList.remove('theme-switch'); }
    );
  });
})();
