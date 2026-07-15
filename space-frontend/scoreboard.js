// scoreboard.js
// Contains rendering and helper functions for the scoreboard.
// empty scores array
const scores = [];

// url for backend-fetch, insert ip of backend server-api
const apiURL = "http://xxx.xxx.xxx.xxx:8000/scores";

// Updates the animated digital counter for the top score and congratulates the top player
var lastTopScore = 0;
var typingInterval = null;
var typingState = 'idle'; // 'typing', 'deleting', 'idle'
var typingTimeout = null;

function animateTopScoreTyping(scoreStr) {
    var counter = document.getElementById('top-score-counter');
    var i = 0;
    typingState = 'typing';
    function typeNext() {
        counter.textContent = scoreStr.slice(0, i);
        if (i < scoreStr.length) {
            i++;
            typingTimeout = setTimeout(typeNext, 180); // slower typing
        } else {
            typingState = 'idle';
            typingTimeout = setTimeout(function() {
                animateTopScoreDeleting(scoreStr);
            }, 1800); // pause before deleting
        }
    }
    typeNext();
}

function animateTopScoreDeleting(scoreStr) {
    var counter = document.getElementById('top-score-counter');
    var i = scoreStr.length;
    typingState = 'deleting';
    function deleteNext() {
        counter.textContent = scoreStr.slice(0, i);
        if (i > 0) {
            i--;
            typingTimeout = setTimeout(deleteNext, 120); // slower deleting
        } else {
            typingState = 'idle';
            typingTimeout = setTimeout(function() {
                animateTopScoreTyping(scoreStr);
            }, 1200); // pause before re-typing
        }
    }
    deleteNext();
}

// render the scoreboard with the scores array
function renderScoreboard(scores) {
    // Sort scores from highest to lowest and take the top 10
    scores.sort(function(a, b) { return b.score - a.score; });
    var topScores = scores.slice(0, 10);
    console.log(scores);

    // Fill the table body
    var tbody = document.querySelector('#scoreboard tbody');
    tbody.innerHTML = '';
	scores.forEach((entry, i)=> {
	if (i < 10) {
        var tr = document.createElement('tr');
	if ( entry.name == "") {
		tr.innerHTML =
			'<td>ungültige Eingabe</td>'
	} else {
        tr.innerHTML =
            '<td>' + (i + 1) + '</td>' +
            '<td>' + entry.name + '</td>' +
            '<td>' + entry.score + '</td>'
	}
        tbody.appendChild(tr);
	}
    	updateTopScoreCounter(topScores);
    })
}

// update scoreboard entries
async function updateScore() {                                                                   
        try {                                                                                    
                let response = await fetch(apiURL);
                let data = await response.text();
                let scores = await JSON.parse(data);

		renderScoreboard(scores);

        } catch (err) {                                                                          
                showError('Fehler beim Laden der Daten: ' + err.message);
		console.log(err);
        }                                                                                        
}; 
// interval for fetch
setInterval(updateScore, 10000);

function updateTopScoreCounter(scores) {
    var counter = document.getElementById('top-score-counter');
    var congrats = document.getElementById('top-score-congrats');
    var topScore = (scores && scores.length > 0) ? scores[0].score : 0;
    var topPlayer = (scores && scores.length > 0) ? scores[0].name : null;
    var toStr = String(topScore);

    // If the score changed, restart the animation
    if (toStr !== String(lastTopScore)) {
        if (typingTimeout) clearTimeout(typingTimeout);
        animateTopScoreTyping(toStr);
    }
    lastTopScore = topScore;

    // Show/hide congratulation message
    if (topPlayer) {
        congrats.textContent = 'Congratulations, ' + topPlayer + '!';
        congrats.classList.remove('hidden');
        congrats.classList.add('visible');
    } else {
        congrats.textContent = '';
        congrats.classList.add('hidden');
        congrats.classList.remove('visible');
    }
}

// Show error message
function showError(message) {
    var errorDiv = document.getElementById('error-message');
    errorDiv.textContent = message;
    errorDiv.classList.remove('hidden');
}

// Updates the last updated time
function updateRefreshIndicator() {
    var now = new Date();
    var formatted = now.toLocaleTimeString();
    document.getElementById('last-updated').textContent = formatted;
}

// Creates a simple animated star background
function createStars(numStars) {
    var starBg = document.getElementById('star-bg');
    if (!starBg) return;
    starBg.innerHTML = '';
    for (var i = 0; i < numStars; i++) {
        var star = document.createElement('div');
        star.className = 'star';
        var size = Math.random() * 2 + 1;
        star.style.width = size + 'px';
        star.style.height = size + 'px';
        star.style.top = (Math.random() * 100) + '%';
        star.style.left = (Math.random() * 100) + '%';
        star.style.animationDuration = (2 + Math.random() * 4) + 's';
        starBg.appendChild(star);
    }
}

// Theme toggle: cycles through three themes
var THEMES = ['light', 'dark', 'futuristic'];
var currentThemeIdx = 0;
function setTheme(theme) {
    document.body.setAttribute('data-theme', theme);
}
function cycleTheme() {
    currentThemeIdx = (currentThemeIdx + 1) % THEMES.length;
    setTheme(THEMES[currentThemeIdx]);
}

// Set up everything when the page loads
window.addEventListener('DOMContentLoaded', function() {
    setTheme(THEMES[0]);
    var toggle = document.getElementById('theme-toggle');
    if (toggle) toggle.onclick = cycleTheme;
    createStars(80);
}); 
