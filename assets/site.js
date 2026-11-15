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
})();
