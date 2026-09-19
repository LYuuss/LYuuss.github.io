(() => {
  'use strict';
  const root = document.documentElement;
  const theme = document.querySelector('.theme-toggle');
  const isEnglish = root.lang === 'en';
  const syncTheme = () => {
    const dark = root.dataset.theme === 'dark';
    theme.setAttribute('aria-pressed', String(dark));
    theme.setAttribute('aria-label', isEnglish ? `Switch to ${dark ? 'light' : 'dark'} theme` : `Activer le thème ${dark ? 'clair' : 'sombre'}`);
    theme.querySelector('span').textContent = dark ? theme.dataset.light : theme.dataset.dark;
    document.querySelector('meta[name="theme-color"]').content = dark ? '#14171c' : '#fafbfc';
  };
  if (theme) {
    theme.hidden = false;
    syncTheme();
    theme.addEventListener('click', () => {
      root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem('lyes-theme', root.dataset.theme); } catch (_) {}
      syncTheme();
    });
  }
  const print = document.querySelector('.print-button');
  if (print) {
    print.hidden = false;
    print.addEventListener('click', () => window.print());
  }
  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
  // Keep the section being read when changing language; links work without JS.
  const languageLinks = document.querySelectorAll('.language-switch a');
  const syncLanguageLinks = () => {
    languageLinks.forEach(link => {
      const url = new URL(link.getAttribute('href'), window.location.href);
      url.hash = window.location.hash;
      link.href = url.href;
    });
  };
  syncLanguageLinks();
  window.addEventListener('hashchange', syncLanguageLinks);
})();
