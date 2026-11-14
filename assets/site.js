// Sprachwahl merken und beim Wechsel zur selben Seite in der anderen Sprache gehen
(function () {
  var select = document.querySelector('.lang');
  if (select) {
    try { localStorage.setItem('ks-lang', document.documentElement.lang); } catch (e) {}
    select.addEventListener('change', function () {
      var option = select.options[select.selectedIndex];
      try { localStorage.setItem('ks-lang', option.getAttribute('data-lang')); } catch (e) {}
      location.href = option.value;
    });
  }

  // Sucher auf der Startseite: das Flugzeug fliegt, der Rahmen folgt, der Ausschnitt folgt weich
  var finder = document.querySelector('.finder');
  if (!finder) return;
  var plane = finder.querySelector('.plane'), box = finder.querySelector('.box'), crop = finder.querySelector('.crop');
  var still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var cx = 0.5, cy = 0.5, cs = 0.62, last = null, t = 0;
  function place(el, x, y, w, h, W, H) {
    el.style.width = w * W + 'px';
    el.style.height = h * H + 'px';
    el.style.transform = 'translate(' + (x - w / 2) * W + 'px,' + (y - h / 2) * H + 'px)';
  }
  function frame(now) {
    var dt = last === null ? 0 : Math.min((now - last) / 1000, 0.05);
    last = now;
    t += dt;
    var W = finder.clientWidth, H = finder.clientHeight;
    // Flugbahn und scheinbare Grösse des Flugzeugs
    var px = 0.5 + 0.3 * Math.sin(t * 0.45), py = 0.47 + 0.16 * Math.sin(t * 0.7 + 1);
    var size = 0.13 + 0.05 * Math.sin(t * 0.3);
    var pw = size, ph = size * 0.42 * W / H;
    plane.style.width = pw * W + 'px';
    plane.style.transform = 'translate(' + (px - pw / 2) * W + 'px,' + (py * H - pw * W * 0.21) + 'px)';
    place(box, px, py, pw * 1.25, ph * 1.7, W, H);
    // Ausschnitt des virtuellen Gimbals: folgt gedämpft, lässt Rand frei
    var k = 1 - Math.exp(-dt / 0.6), ks = 1 - Math.exp(-dt / 1.6);
    var want = Math.min(Math.max(size * 3.4, 0.45), 0.8);
    cs += (want - cs) * ks;
    cx += (px - cx) * k;
    cy += (py - cy) * k;
    var hx = cs / 2, hy = cs / 2;
    cx = Math.min(Math.max(cx, hx), 1 - hx);
    cy = Math.min(Math.max(cy, hy), 1 - hy);
    place(crop, cx, cy, cs, cs, W, H);
    if (!still) requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
  if (still) window.addEventListener('resize', function () { last = null; requestAnimationFrame(frame); });
})();
