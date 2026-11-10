// Alternância de tema (claro/escuro) e idioma (PT/EN), com preferência salva no navegador.
// O estado inicial é definido por um script inline no <head> (evita "flash" ao carregar).
(function () {
  'use strict';

  var root = document.documentElement;

  function save(key, value) {
    try {
      localStorage.setItem(key, value);
    } catch (e) {
      /* armazenamento indisponível (modo privado, etc.) */
    }
  }

  function applyLang(lang) {
    lang = lang === 'en' ? 'en' : 'pt';
    root.dataset.lang = lang;
    root.lang = lang === 'en' ? 'en' : 'pt-BR';
    var title = document.body.getAttribute('data-title-' + lang);
    if (title) document.title = title;
    save('lang', lang);
  }

  function applyTheme(theme) {
    root.dataset.theme = theme === 'dark' ? 'dark' : 'light';
    save('theme', root.dataset.theme);
  }

  applyLang(root.dataset.lang);

  var langBtn = document.getElementById('lang-toggle');
  if (langBtn) {
    langBtn.addEventListener('click', function () {
      applyLang(root.dataset.lang === 'pt' ? 'en' : 'pt');
    });
  }

  var themeBtn = document.getElementById('theme-toggle');
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      applyTheme(root.dataset.theme === 'dark' ? 'light' : 'dark');
    });
  }

  document.querySelectorAll('.js-print').forEach(function (btn) {
    btn.addEventListener('click', function () {
      window.print();
    });
  });
})();
