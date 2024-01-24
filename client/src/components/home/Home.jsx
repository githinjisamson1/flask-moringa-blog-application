import React from "react";
import "./home.css";
import Navbar from "./Navbar";
import Hero from "./Hero";
import About from "./About";
import Footer from "./Footer";

const Home = () => {
  return (
    <div className="home">
      <Navbar />
      <Hero />
      <About />
      <Footer />
    </div>
  );
};

export default Home;
