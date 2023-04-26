import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const handleClick = () => {
    console.log('Button clicked');
  }

  return (
    <div className="App">
      <header className="App-header">
        <button onClick={handleClick}>
            Test
        </button>
      </header>
    </div>
  );
}

export default App;
