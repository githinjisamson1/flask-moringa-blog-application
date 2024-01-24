import React from "react";
import "./navbar.css";
import moringaLogo from "../../assets/moringaLogo.png";

const Navbar = () => {
  return (
    <div className="navbar">
      <div className="logo">
        <img src={moringaLogo} alt="" />
      </div>

      <div className="register-login-btns">
        <button className="signin">Sign in</button>
        <button className="register">Get started</button>
      </div>
    </div>
  );
};

export default Navbar;
