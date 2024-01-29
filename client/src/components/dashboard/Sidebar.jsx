import React from "react";
import "./sidebar.css";
import SchoolIcon from "@mui/icons-material/School";
import HtmlIcon from "@mui/icons-material/Html";
import JavascriptIcon from "@mui/icons-material/Javascript";
import { useGlobalContext } from "../../context/postsContext";

const Sidebar = () => {
  // Destructuring the filterPostByPhase
  const { filterPostByPhase } = useGlobalContext();

  return (
    <div className="sidebar">
      <ul className="phases">
        <li
          onClick={() => {
            filterPostByPhase("All");
          }}
        >
          <i className="fa-brands fa-html5"></i>
          View All
        </li>
        <li
          onClick={() => {
            filterPostByPhase(0);
          }}
        >
          <i className="fa-brands fa-html5"></i>
          Phase 0
        </li>
        <li
          onClick={() => {
            filterPostByPhase(1);
          }}
        >
          {" "}
          <i className="fa-brands fa-js"></i>
          Phase 1
        </li>
        <li
          onClick={() => {
            filterPostByPhase(2);
          }}
        >
          {" "}
          <i className="fa-brands fa-react"></i>
          Phase 2
        </li>
        <li
          onClick={() => {
            filterPostByPhase(3);
          }}
        >
          {" "}
          <i className="fa-brands fa-python"></i>
          Phase 3
        </li>
        <li
          onClick={() => {
            filterPostByPhase(4);
          }}
        >
          {" "}
          <i className="fa-solid fa-flask"></i>
          Phase 4
        </li>
        <li
          onClick={() => {
            filterPostByPhase(5);
          }}
        >
          {" "}
          <i className="fa-solid fa-diagram-project"></i>
          Phase 5
        </li>
      </ul>
    </div>
  );
};

export default Sidebar;
