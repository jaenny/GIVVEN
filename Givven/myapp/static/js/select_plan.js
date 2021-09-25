var cards = document.querySelectorAll('.card');

cards.forEach(function (el) {
  el.addEventListener('click', changeValue);
});

function changeValue(el) {
  var cardTarget = el.currentTarget;
  var select = cardTarget.childNodes[3];

  cards.forEach(function (el) {
    el.classList.remove('activate');
    el.childNodes[3].classList.remove('select-activate');
  });

  cardTarget.classList.add('activate');
  select.classList.add('select-activate');
  document.querySelector('#plan').value = cardTarget.classList[1];
  document.querySelector('#test').classList.add('activate');
}
