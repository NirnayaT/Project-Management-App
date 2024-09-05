import React, { useState } from 'react';
import axios from 'axios';
import { useLocation, useNavigate } from 'react-router-dom';

const ResetPassword = () => {
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const location = useLocation();
  const navigate = useNavigate();

  const query = new URLSearchParams(location.search);
  const token = query.get('token');

  const validatePassword = (password) => {
    const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    return passwordPattern.test(password);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Reset the error message
    setError('');

    // Check if the passwords match first
    if (newPassword !== confirmPassword) {
      setError('Passwords do not match');
      return;
    }

    // If passwords match, check the password complexity
    if (!validatePassword(newPassword)) {
      setError('Password must contain at least one uppercase letter, one lowercase letter, one digit, one special character, and be at least 8 characters long.');
      return;
    }

    // Proceed with the password reset request if validation passes
    try {
      await axios.post('http://127.0.0.1:8000/api/v1/user/reset-password', {
        token,
        new_password: newPassword,
        confirm_password: confirmPassword,
      });
      navigate('/password-reset-success'); // Redirect to a success page
    } catch (error) {
      setError('Failed to reset password');
    }
  };

  return (
    <div>
      <h2>Reset Password</h2>
      <p id="error-message" className={error ? 'active' : ''}>{error}</p>
      <form onSubmit={handleSubmit}>
        <label>
          New Password:
          <input
            type="password"
            value={newPassword}
            onChange={(e) => setNewPassword(e.target.value)}
            required
          />
        </label>
        <br />
        <label>
          Confirm Password:
          <input
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
          />
        </label>
        <br />
        <button type="submit">Reset Password</button>
      </form>
    </div>
  );
};

export default ResetPassword;
