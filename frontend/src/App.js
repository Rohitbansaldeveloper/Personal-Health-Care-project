import React, { useState } from 'react';

function App() {
  const [pid, setPid] = useState('');
  const [name, setName] = useState('');

  const register = async () => {
    const res = await fetch(`/register?name=${name}`, { method: 'POST' });
    const data = await res.json();
    setPid(data.pid);
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>HealthCare Portal</h1>
      {!pid ? (
        <div>
          <input onChange={(e) => setName(e.target.value)} placeholder="Enter Name" />
          <button onClick={register}>Get Patient ID (PID)</button>
        </div>
      ) : (
        <div>
          <h3>Your PID: <strong>{pid}</strong></h3>
          <p>Use this ID for all appointments and reports.</p>
          {/* Appointment booking form goes here */}
        </div>
      )}
    </div>
  );
}

export default App;
