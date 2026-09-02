(function () {
  var root = document.documentElement;
  var btn = document.getElementById('theme-toggle');
  if (!btn) return;

  function current() {
    return root.getAttribute('data-theme') ||
      (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  }

  function apply(next) {
    root.setAttribute('data-theme', next);
    btn.setAttribute('aria-pressed', String(next === 'dark'));
    try { localStorage.setItem('theme', next); } catch (e) {}
  }

  btn.setAttribute('aria-pressed', String(current() === 'dark'));

  btn.addEventListener('click', function () {
    var next = current() === 'dark' ? 'light' : 'dark';
    if (!document.startViewTransition) return apply(next);

    root.classList.add('theme-switch');
    var vt = document.startViewTransition(function () { apply(next); });
    vt.finished.then(function () { root.classList.remove('theme-switch'); },
                     function () { root.classList.remove('theme-switch'); });
  });
})();
