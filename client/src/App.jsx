import React from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./components/home/Home";
import Signup from "./components/signup/Signup";
import Signin from "./components/signin/Signin";
import Dashboard from "./components/dashboard/Dashboard";
import CreatePost from "./components/createPost/CreatePost";

// routes
const App = () => {
  return (
    <div>
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route exact path="/signup" element={<Signup />} />
        <Route exact path="/signin" element={<Signin />} />
        <Route exact path="/dashboard" element={<Dashboard />} />
        <Route exact path="/createPost" element={<CreatePost />} />
      </Routes>
    </div>
  );
};

export default App;
