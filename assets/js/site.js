/* Theme toggle, sidebar disclosure, mobile nav, and client-side search.
   No dependencies, no network calls beyond the one search index fetch. */

(function () {
  'use strict';

  /* ---------------------------------------------------------- theme */
  var root = document.documentElement;

  function currentTheme() {
    var set = root.getAttribute('data-theme');
    if (set === 'light' || set === 'dark') return set;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  var toggle = document.querySelector('.theme-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var next = currentTheme() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('theme', next); } catch (e) {}
    });
  }

  /* -------------------------------------------------- sidebar folding */
  document.querySelectorAll('.nav .disclose').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var li = btn.closest('li');
      var open = li.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });

  var navToggle = document.querySelector('.nav-toggle');
  if (navToggle) {
    navToggle.addEventListener('click', function () {
      var open = document.body.classList.toggle('nav-open');
      navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // keep the active sidebar item in view on load
  var active = document.querySelector('.nav a.active');
  if (active) {
    var side = document.getElementById('sidebar');
    if (side && active.offsetTop > side.clientHeight - 80) {
      side.scrollTop = active.offsetTop - side.clientHeight / 2;
    }
  }

  /* --------------------------------------------------------- search */
  var input = document.getElementById('search-input');
  var out = document.getElementById('search-results');
  if (!input || !out) return;

  var index = null, loading = false, sel = -1;

  function load() {
    if (index || loading) return Promise.resolve();
    loading = true;
    return fetch(indexURL())
      .then(function (r) { return r.json(); })
      .then(function (d) { index = d; })
      .catch(function () { index = []; })
      .finally(function () { loading = false; });
  }

  function indexURL() {
    var base = document.querySelector('link[rel=canonical]');
    var origin = location.origin;
    if (base) { try { origin = new URL(base.href).origin; } catch (e) {} }
    // site may be served from a subpath (project Pages); derive it from the brand link
    var brand = document.querySelector('.brand');
    var prefix = brand ? new URL(brand.href).pathname.replace(/\/$/, '') : '';
    return origin + prefix + '/index.json';
  }

  function esc(s) {
    return s.replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function score(page, terms) {
    var t = page.t.toLowerCase(),
        d = (page.d || '').toLowerCase(),
        b = (page.b || '').toLowerCase(),
        s = 0;
    for (var i = 0; i < terms.length; i++) {
      var q = terms[i];
      if (!q) continue;
      var inT = t.indexOf(q), inD = d.indexOf(q), inB = b.indexOf(q);
      if (inT < 0 && inD < 0 && inB < 0) return 0;      // every term must appear
      if (inT === 0) s += 60; else if (inT > 0) s += 34;
      if (inD >= 0) s += 9;
      if (inB >= 0) s += 4;
    }
    return s;
  }

  function snippet(page, terms) {
    var b = page.b || page.d || '';
    var low = b.toLowerCase(), at = -1;
    for (var i = 0; i < terms.length && at < 0; i++) at = low.indexOf(terms[i]);
    if (at < 0) return esc(b.slice(0, 130));
    var from = Math.max(0, at - 45);
    var text = (from ? '…' : '') + b.slice(from, from + 160) + '…';
    var html = esc(text);
    terms.forEach(function (q) {
      if (!q) return;
      html = html.replace(new RegExp('(' + q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'),
                          '<mark>$1</mark>');
    });
    return html;
  }

  function render(hits, terms) {
    sel = -1;
    if (!hits.length) {
      out.innerHTML = '<div class="empty">No pages match that.</div>';
      out.hidden = false;
      return;
    }
    out.innerHTML = hits.map(function (h) {
      return '<a href="' + h.u + '">' +
             (h.s ? '<div class="r-crumb">' + esc(h.s.replace(/-/g, ' ')) + '</div>' : '') +
             '<div class="r-title">' + esc(h.t) + '</div>' +
             '<div class="r-snip">' + snippet(h, terms) + '</div></a>';
    }).join('');
    out.hidden = false;
  }

  function run() {
    var q = input.value.trim().toLowerCase();
    if (q.length < 2) { out.hidden = true; return; }
    var terms = q.split(/\s+/);
    var hits = (index || [])
      .map(function (p) { return { p: p, s: score(p, terms) }; })
      .filter(function (x) { return x.s > 0; })
      .sort(function (a, b) { return b.s - a.s; })
      .slice(0, 12)
      .map(function (x) { return x.p; });
    render(hits, terms);
  }

  input.addEventListener('focus', load);
  input.addEventListener('input', function () { load().then(run); });

  input.addEventListener('keydown', function (e) {
    var items = out.querySelectorAll('a');
    if (e.key === 'Escape') { out.hidden = true; input.blur(); return; }
    if (!items.length || out.hidden) return;
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault();
      if (sel >= 0) items[sel].classList.remove('sel');
      sel = e.key === 'ArrowDown'
        ? (sel + 1) % items.length
        : (sel - 1 + items.length) % items.length;
      items[sel].classList.add('sel');
      items[sel].scrollIntoView({ block: 'nearest' });
    } else if (e.key === 'Enter' && sel >= 0) {
      e.preventDefault();
      location.href = items[sel].href;
    }
  });

  document.addEventListener('click', function (e) {
    if (!e.target.closest('.search')) out.hidden = true;
  });

  // "/" focuses search, the way every docs site does
  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) {
      e.preventDefault();
      input.focus();
    }
  });
})();
