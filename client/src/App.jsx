import React from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./components/home/Home";
import Signup from "./components/home/Signup";
import Signin from "./components/home/Signin";
// npm install @mui/icons-material @mui/material @emotion/styled @emotion/react

const App = () => {
  return (
    <div>
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route exact path="/signup" element={<Signup />} />
        <Route exact path="/signin" element={<Signin />} />
      </Routes>
    </div>
  );
};

export default App;
