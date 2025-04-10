import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import EmployeeRegistration from './admin/EmployeeRegistration';
import FormUsageStatistics from './admin/FormUsageStatistics';

function AdminViews() {
  return (
    <div>
      <h2>Admin Portal</h2>
      <nav>
        <Link to="register-employee">Register Employee</Link>
        <Link to="form-statistics">Form Usage Statistics</Link>
      </nav>

      <Routes>
        <Route path="register-employee" element={<EmployeeRegistration />} />
        <Route path="form-statistics" element={<FormUsageStatistics />} />
      </Routes>
    </div>
  );
}

export default AdminViews;