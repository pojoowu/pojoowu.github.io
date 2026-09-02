(function () {
  var root = document.documentElement;
  var btn = document.getElementById('theme-toggle');
  if (!btn) return;

  function getStoredTheme() {
    try { return localStorage.getItem('theme'); } catch (e) { return null; }
  }

  function preferredTheme() {
    return getStoredTheme() ||
      (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  }

  function currentTheme() {
    return root.getAttribute('data-theme') || preferredTheme();
  }

  function render(theme) {
    root.setAttribute('data-theme', theme);
    btn.setAttribute('aria-pressed', String(theme === 'dark'));
  }

  function applyTheme(next) {
    render(next);
    try { localStorage.setItem('theme', next); } catch (e) {}
  }

  // Re-read the stored theme whenever this document is (re)shown. A prerendered
  // page ran the inline head script early, and a page restored from the
  // back/forward cache keeps its old attribute, so both are stale if the theme
  // was toggled in the meantime. `pagereveal` fires before the incoming page is
  // captured for the cross-document view transition, so the correction is
  // never visible.
  function syncFromStorage() { render(preferredTheme()); }

  render(currentTheme());
  window.addEventListener('pagereveal', syncFromStorage);
  window.addEventListener('pageshow', function (e) { if (e.persisted) syncFromStorage(); });
  window.addEventListener('storage', function (e) { if (e.key === 'theme') syncFromStorage(); });

  btn.addEventListener('click', function () {
    var next = currentTheme() === 'dark' ? 'light' : 'dark';

    if (!document.startViewTransition) {
      applyTheme(next);
      return;
    }

    // While .theme-switch is set the masthead has no view-transition-name
    // (see transitions.css), so header and content crossfade together.
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
