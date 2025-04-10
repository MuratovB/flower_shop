import React, { useState } from 'react';

function EmployeeRegistration() {
  const [employeeData, setEmployeeData] = useState({
    firstName: '',
    lastName: '',
    position: '',
    login: '',
    password: ''
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Registering employee:', employeeData);
  };

  return (
    <div>
      <h3>Employee Registration</h3>
      <form onSubmit={handleSubmit}>
        <div>
          <label>First Name:</label>
          <input 
            type="text" 
            value={employeeData.firstName}
            onChange={(e) => setEmployeeData({...employeeData, firstName: e.target.value})}
            required
          />
        </div>
        <div>
          <label>Last Name:</label>
          <input 
            type="text" 
            value={employeeData.lastName}
            onChange={(e) => setEmployeeData({...employeeData, lastName: e.target.value})}
            required
          />
        </div>
        <div>
          <label>Position:</label>
          <input 
            type="text" 
            value={employeeData.position}
            onChange={(e) => setEmployeeData({...employeeData, position: e.target.value})}
            required
          />
        </div>
        <div>
          <label>Login:</label>
          <input 
            type="text" 
            value={employeeData.login}
            onChange={(e) => setEmployeeData({...employeeData, login: e.target.value})}
            required
          />
        </div>
        <div>
          <label>Password:</label>
          <input 
            type="password" 
            value={employeeData.password}
            onChange={(e) => setEmployeeData({...employeeData, password: e.target.value})}
            required
          />
        </div>
        <button type="submit">Register Employee</button>
      </form>
    </div>
  );
}

export default EmployeeRegistration;