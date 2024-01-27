import React from "react";
import "./aside.css";
import createPostCardImage from "../../assets/createPostCardImage.avif";

const Aside = () => {
  return (
    <div className="dashboard-aside">
      <div className="create-post-card">
        {/* top */}
        <div className="create-post-card-img">
          <img src={createPostCardImage} alt="" />
        </div>

        {/* middle */}
        <div className="create-post-card-body">
          <h3>
            <i class="fa-solid fa-code"></i>
            Home
          </h3>
          <p>Moringa Blog frontpage.</p>
        </div>

        {/* bottom */}
        <div className="create-post-card-btn">
          <button>Create Post</button>
        </div>
      </div>
    </div>
  );
};

export default Aside;
