import React from "react";
import "./singleComment.css";

const SingleComment = () => {
  return (
    <div className="comment">
      <div className="comment-author-time">
        <h3 className="author">Author</h3>
        <p className="time">3hr ago</p>
      </div>

      <div className="comment-content">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Veniam odit
        iure illum dignissimos, quam accusamus voluptates officiis sed animi
        vero suscipit esse asperiores dicta soluta atque qui? Quidem, fuga!
        Neque.
      </div>
    </div>
  );
};

export default SingleComment;
