import React, { useState } from "react";
import "./singlePost.css";
import ThumbUpIcon from "@mui/icons-material/ThumbUp";
import ThumbDownIcon from "@mui/icons-material/ThumbDown";
import CommentIcon from "@mui/icons-material/Comment";
import { useGlobalUserContext } from "../../context/authContext";

const SinglePost = ({
  id,
  title,
  phase,
  content,
  created_at,
  resources,
  user,
  votes,
  comments,
}) => {
  // const { currentUser } = useGlobalUserContext();
  // console.log(`CurrentUser: ${currentUser}`);
  console.log(localStorage.getItem("auth_token"))

  const [isFullTextVisible, setIsFullTextVisible] = useState(false);

  const toggleReadMore = () => {
    setIsFullTextVisible(!isFullTextVisible);
  };

  // console.log(votes[0].vote_type);

  const numberOfVotes = votes.filter((vote) => {
    return vote.vote_type === true;
  });

  return (
    <div className="single-post">
      <div className="post-owner">
        <h4>{user.full_name}</h4>
        <p>Phase: {phase}</p>
      </div>

      <div className="title">
        <h3>{title}</h3>
      </div>

      <div className="post-content">
        {isFullTextVisible ? (
          <div>{content}</div>
        ) : (
          <div>
            {content.length > 300 ? `${content.slice(0, 300)}` : content}
          </div>
        )}
        {content.length > 300 && (
          <span className="read-more" onClick={toggleReadMore}>
            {isFullTextVisible ? "Read Less" : "Read More"}
          </span>
        )}
      </div>

      <div className="post-bottom">
        <div className="vote-details">
          <ThumbUpIcon
            onClick={() => {
              fetch("/votes", {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                  // Authorization: `Bearer ${currentUser.auth_token}`,
                  Authorization: `Bearer ${localStorage.getItem("auth_token")}`,
                  Accept: "application/json",
                },
                body: JSON.stringify({
                  vote_type: 1,
                  // user_id: currentUser.data.id, //passed on the server side
                  post_id: id,
                }),
              })
                .then((response) => {
                  return response.json();
                })
                .then((data) => {
                  console.log(data);
                })
                .catch((error) => {
                  console.log(error);
                });
            }}
          />
          <span>{numberOfVotes.length}</span>
          <ThumbDownIcon />
        </div>
        <div className="comment-details">
          <CommentIcon />
          <span>{comments.length}</span>
        </div>
      </div>
    </div>
  );
};

export default SinglePost;
