// import { Navigate, Outlet } from 'react-router-dom';
// import {jwtDecode} from 'jwt-decode';
// import { useState, useEffect } from 'react';
// import dayjs from 'dayjs';

// interface DecodedToken {
//   exp: number; // Adjust based on your token's payload
// }

// const Protected: React.FC = () => {
//   const [isTokenValid, setIsTokenValid] = useState<boolean>(true);

//   useEffect(() => {
//     const access_token = localStorage.getItem('access_token');
//     if (access_token) {
//       try {
//         const decoded = jwtDecode(access_token);
//         console.log("decodedd",decoded)
//         const isExpired = dayjs().isAfter(dayjs.unix(decoded.expiry));

//         if (isExpired) {
//           localStorage.removeItem('access_token');
//           localStorage.removeItem('refresh_token');
//           setIsTokenValid(false);
//         }
//       } catch (e) {
//         console.error('Invalid token', e);
//         setIsTokenValid(false);
//       }
//     } else {
//       setIsTokenValid(false);
//     }
//   }, []);

//   return isTokenValid ? <Outlet /> : <Navigate to="/" />;
// };

// export default Protected;
