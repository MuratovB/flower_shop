import React, { useState } from 'react';

function LoginForm({ onLogin }) {
  const [credentials, setCredentials] = useState({
    login: '',
    password: ''
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    const userData = {
      id: 1,
      name: 'Test User',
      role: 'customer'
    };
    onLogin(userData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Login:</label>
        <input 
          type="text" 
          value={credentials.login}
          onChange={(e) => setCredentials({...credentials, login: e.target.value})}
        />
      </div>
      <div>
        <label>Password:</label>
        <input 
          type="password" 
          value={credentials.password}
          onChange={(e) => setCredentials({...credentials, password: e.target.value})}
        />
      </div>
      <button type="submit">Login</button>
    </form>
  );
}

export default LoginForm;