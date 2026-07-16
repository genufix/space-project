const scores = [
  { player: "Oliver", score: 500 },
  { player: "Peter", score: 300 },
  { player: "Peter", score: 200 },
];

function renderScoreboard(scores) {
  const tbody = document.querySelector("#scoreboard tbody");
  tbody.innerHTML = "";
  scores.forEach(function (entry, idx) {
    const tr = document.createElement("tr");
    tr.innerHTML =
      "<td>" +
      (idx + 1) +
      "</td>" +
      "<td>" +
      entry.name +
      "</td>" +
      "<td>" +
      entry.score +
      "</td>";
    tbody.appendChild(tr);
  });
}
function showError(message) {
  const errorBox = document.getElementById("error-message");

  errorBox.textContent = message;

  errorBox.classList.remove("hidden");

  setTimeout(() => {
    errorBox.classList.add("hidden");
  }, 3000);
}

showError("Hoppla! Ein unerwarteter Fehler ist aufgetreten.");

async function updateScore() {
  try {
    let response = await fetch(apiURL);
    let data = await response.text();
    let scores = await JSON.parse(data);

    renderScoreboard(scores);
  } catch (err) {
    showError("Fehler beim Laden der Daten: " + err.message);
  }
}

function abfrageSenden() {
  console.log("Die Abfrage wurde ausgeführt!");
}

const meinIntervall = setInterval(abfrageSenden, 5000);

var THEMES = ["light", "dark", "futuristic"];
var currentThemeIdx = 0;
function setTheme(theme) {
  document.body.setAttribute("data-theme", theme);
}
const themeBtn = document.getElementById("theme-toggle");
const body = document.body;

themeBtn.addEventListener("click", () => {
  const currentTheme = body.getAttribute("data-theme");

  if (currentTheme === "dark") {
    body.setAttribute("data-theme", "light");
  } else {
    body.setAttribute("data-theme", "dark");
  }
});

function animateScore(targetScore) {
  const display = document.getElementById("top-score-display");
  const congrats = document.getElementById("congrats-message");

  let currentScore = 0;

  const speed = 15;

  const step = Math.ceil(targetScore / 100);

  const counter = setInterval(() => {
    currentScore += step;

    if (currentScore >= targetScore) {
      display.innerText = targetScore;
      clearInterval(counter);

      congrats.classList.remove("hidden");
    } else {
      display.innerText = currentScore;
    }
  }, speed);
}

window.addEventListener("DOMContentLoaded", () => {
  animateScore(500);
});

function createStars() {
  const container = document.getElementById("stars-container");
  if (!container) return;

  const numberOfStars = 100;

  for (let i = 0; i < numberOfStars; i++) {
    const star = document.createElement("div");
    star.classList.add("star");

    const x = Math.random() * 100;
    const y = Math.random() * 100;
    star.style.left = `${x}%`;
    star.style.top = `${y}%`;

    const size = Math.random() * 2 + 1;
    star.style.width = `${size}px`;
    star.style.height = `${size}px`;

    const delay = Math.random() * 3;
    star.style.animationDelay = `${delay}s`;

    container.appendChild(star);
  }
}

window.addEventListener("DOMContentLoaded", () => {
  console.log("DOM ist geladen, starte Sterne-Generierung...");

  createStars();

  if (typeof animateScore === "function") {
    animateScore(500);
  }
});

function createStars() {
  console.log("createStars() wurde gestartet!");
  const container = document.getElementById("stars-container");

  if (!container) {
    console.error(
      "FEHLER: Der Container '#stars-container' wurde im HTML nicht gefunden!",
    );
    return;
  }

  const numberOfStars = 100;
  console.log(`Erstelle jetzt ${numberOfStars} Sterne...`);

  for (let i = 0; i < numberOfStars; i++) {
    const star = document.createElement("div");
    star.classList.add("star");

    // Zufällige Position
    const x = Math.random() * 100;
    const y = Math.random() * 100;
    star.style.left = x + "%";
    star.style.top = y + "%";
    const size = Math.random() * 2 + 1 + "px";
    star.style.width = size;
    star.style.height = size;

    const delay = Math.random() * 3 + "s";
    star.style.animationDelay = delay;

    container.appendChild(star);
  }
  console.log("Sterne erfolgreich generiert und eingefügt!");
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", createStars);
} else {
  // Falls die Seite schon fertig geladen war
  createStars();
}
