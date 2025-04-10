import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import CustomerViews from './components/CustomerViews';
import SalesManagerViews from './components/SalesManagerViews';
import SuppliesManagerViews from './components/SuppliesManagerViews';
import AccountantViews from './components/AccountantViews';
import AdminViews from './components/AdminViews';
import LoginForm from './components/common/LoginForm';

function App() {
  const [currentUser, setCurrentUser] = useState(null);
  const [userRole, setUserRole] = useState(null);

  const handleLogin = (userData) => {
    setCurrentUser(userData);
    setUserRole(userData.role);
  };

  const handleLogout = () => {
    setCurrentUser(null);
    setUserRole(null);
  };

  return (
    <Router>
      <div>
        <nav>
          {currentUser ? (
            <>
              <span>Logged in as: {currentUser.name} ({userRole})</span>
              <button onClick={handleLogout}>Logout</button>
              <Link to="/">Home</Link>
            </>
          ) : (
            <Link to="/login">Login</Link>
          )}
        </nav>

        <Routes>
          <Route path="/login" element={<LoginForm onLogin={handleLogin} />} />
          
          {userRole === 'customer' && (
            <Route path="/*" element={<CustomerViews />} />
          )}
          
          {userRole === 'sales_manager' && (
            <Route path="/*" element={<SalesManagerViews />} />
          )}
          
          {userRole === 'supplies_manager' && (
            <Route path="/*" element={<SuppliesManagerViews />} />
          )}
          
          {userRole === 'accountant' && (
            <Route path="/*" element={<AccountantViews />} />
          )}
          
          {userRole === 'admin' && (
            <Route path="/*" element={<AdminViews />} />
          )}
          
          <Route path="/" element={
            currentUser ? (
              <div>Welcome to the system</div>
            ) : (
              <div>Please log in to access the system</div>
            )
          } />
        </Routes>
      </div>
    </Router>
  );
}

export default App;