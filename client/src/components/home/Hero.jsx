import React from "react";
import "./hero.css";
import { useNavigate } from "react-router-dom";

const Hero = () => {
  const navigate = useNavigate();

  return (
    <div className="hero-container">
      <div className="hero">
        <h1 className="stay-curious">Stay curious.</h1>
        <p className="discover">
          Discover code, thinking, and expertise from engineers on any topic.
        </p>
        <div className="start-reading-container">
          <button
            className="start-reading"
            onClick={() => {
              navigate("/signup");
            }}
          >
            Start Reading
          </button>
        </div>
      </div>
    </div>
  );
};

export default Hero;
