var cards = document.querySelectorAll(".card");
const exPlan = document.querySelector("#exPlan").innerText;

initPlan();

function initPlan() {
  cards.forEach(function (el) {
    if (el.classList[1] === exPlan) {
      el.classList.add("activate");
      const exSelect = el.childNodes[3];
      exSelect.classList.add("select-activate");
      document.querySelector("#plan").value = el.classList[1];
      document.querySelector("#plan-choice-done").classList.add("activate");
    }
  });
}

cards.forEach(function (el) {
  el.addEventListener("click", changeValue);
});

function changeValue(el) {
  var cardTarget = el.currentTarget;
  var select = cardTarget.childNodes[3];

  cards.forEach(function (el) {
    el.classList.remove("activate");
    el.childNodes[3].classList.remove("select-activate");
  });

  cardTarget.classList.add("activate");
  select.classList.add("select-activate");
  document.querySelector("#plan").value = cardTarget.classList[1];
  document.querySelector("#plan-choice-done").classList.add("activate");
}
