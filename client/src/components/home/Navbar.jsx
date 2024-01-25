import React from "react";
import "./navbar.css";
import moringaLogo from "../../assets/moringaLogo.png";
import { useNavigate } from "react-router-dom";

const Navbar = () => {
  const navigate=useNavigate()
  return (
    <div className="navbar">
      <div className="logo">
        <img src={moringaLogo} alt="" />
      </div>

      <div className="register-login-btns">
        <button className="signin" onClick={()=>{
          navigate("/signin")
        }}>Sign in</button>
        <button className="register" onClick={()=>{
          navigate("/signup")
        }}>Get started</button>
      </div>
    </div>
  );
};

export default Navbar;
