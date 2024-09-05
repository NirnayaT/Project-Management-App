// src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ResetPassword from './Resetpassword';
import PasswordResetSuccess from './PasswordResetSuccess'; // Create this page as well

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/reset-password" element={<ResetPassword />} />
        <Route path="/password-reset-success" element={<PasswordResetSuccess />} />
      </Routes>
    </Router>
  );
}

export default App;
