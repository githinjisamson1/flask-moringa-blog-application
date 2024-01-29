import React from "react";
import Header from "../header/Header";
import Sidebar from "./Sidebar";
import PostListing from "./PostListing";
import Aside from "./Aside";
import "./dashboard.css"

const Dashboard = () => {
  return (
    <div className="dashboard">
      <Header />
      <div className="left-center-right">
        <Sidebar />
        <PostListing />
        <Aside />
      </div>
    </div>
  );
};

export default Dashboard;
