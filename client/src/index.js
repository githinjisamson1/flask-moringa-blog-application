import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import "./styles.css";
import App from "./App";
import { PostsProvider } from "./context/postsContext";

// entry point of program
const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <>
    <BrowserRouter>
      <PostsProvider>
        <App />
      </PostsProvider>
    </BrowserRouter>
  </>
);
