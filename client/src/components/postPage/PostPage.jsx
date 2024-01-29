import React from "react";
import Header from "../header/Header";
import PostView from "./PostView";

// page for viewing SinglePost details
const PostPage = () => {
  return (
    <div className="post-page">
      <Header />
      <PostView />
    </div>
  );
};

export default PostPage;
