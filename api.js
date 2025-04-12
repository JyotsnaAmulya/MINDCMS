// import axios from 'axios';

// const API_BASE = 'http://localhost:8000';

// export const generateContent = async ({ topic, keywords }) => {
//   try {
//     const response = await axios.post(`${API_BASE}/generate`, {
//       topic,
//       keywords,
//     });
//     return response.data;
//   } catch (error) {
//     console.error('Error generating content:', error);
//     return { content: 'Failed to generate content' };
//   }
// };



// import axios from 'axios';

// const API = axios.create({
//   baseURL: process.env.REACT_APP_API_URL,
// });

// export const generateContent = async (data) => {
//   const response = await API.post('/api/v1/content', data);
//   return response.data;
// };

// export const publishContent = async (data) => {
//   const response = await API.post('/api/v1/publish', data);
//   return response.data;
// };


const BASE_URL = "http://127.0.0.1:8000/api/v1";

export const generateContent = async (data) => {
  const response = await fetch(`${BASE_URL}/content`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  return response.json();
};

export const publishContent = async (data) => {
  const response = await fetch(`${BASE_URL}/publish`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  return response.json();
};
