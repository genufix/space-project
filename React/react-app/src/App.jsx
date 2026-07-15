import { useState } from "react";
import "./App.css";

function App() {
  const [number, setNumber] = useState(Math.floor(Math.random() * 100) + 1);
  const [guess, setGuess] = useState("");
  const [message, setMessage] = useState("");

  function checkGuess() {
    const userGuess = Number(guess);

    if (userGuess === number) {
      setMessage(" Richtig!");
    } else if (userGuess > number) {
      setMessage("⬇ Zu hoch!");
    } else {
      setMessage("⬆ Zu niedrig!");
    }
  }

  function restart() {
    setNumber(Math.floor(Math.random() * 100) + 1);
    setGuess("");
    setMessage("");
  }

  return (
    <div className="app">
      <div className="card">
        <h1>Zahlen-Raten</h1>

        <p>Rate eine Zahl zwischen 1 und 100</p>

        <form onSubmit={(e) => {
  e.preventDefault();
  checkGuess();
}}>
  <input
    type="number"
    value={guess}
    onChange={(e) => setGuess(e.target.value)}
  />

  <button type="submit">
    Prüfen
  </button>
</form>

        <h2>{message}</h2>

        <button onClick={restart}>
          Neustart
        </button>
      </div>
    </div>
  );
}

export default App;