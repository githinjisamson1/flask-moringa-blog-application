import React from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./components/home/Home";

const App = () => {
  return (
    <div>
      <Routes>
        <Route exact path="/" element={<Home />} />
      </Routes>
    </div>
  );
};

export default App;
