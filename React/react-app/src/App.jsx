import { useState } from "react";
import "./App.css";

function App() {
  const [input, setInput] = useState("");
  const [todos, setTodos] = useState([]);

  function addTodo() {
    if (input.trim() === ""){
      return;
    };

    const newTodo = {
      id: Date.now(),
      text: input,
      done: false
    };

    setTodos([...todos, newTodo]);
  
  setInput("")
  }

  function deleteTodo(id) {
    setTodos(todos.filter((todo) => todo.id !== id));
  }

  function toggleTodo(id) {
     const newTodos = todos.map((todo) => {
    if (todo.id === id) {
      return {
        ...todo,
        done: !todo.done,
      };
    }

    return todo;
  });

  setTodos(newTodos);
    
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>Meine To-Do-Liste</h1>

      <input
        type="text"
        placeholder="Neue Aufgabe..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />

      <button onClick={addTodo}>Hinzufügen</button>

      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            <span>
              {todo.text}
            </span>

            <button onClick={() => toggleTodo(todo.id)}>
              Erledigt
            </button>

            <button onClick={() => deleteTodo(todo.id)}>
              Löschen
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}



export default App;