import React, { useCallback, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "./postView.css";
import ThumbUpIcon from "@mui/icons-material/ThumbUp";
import ThumbDownIcon from "@mui/icons-material/ThumbDown";
import CommentIcon from "@mui/icons-material/Comment";
import { useFormik } from "formik";
import * as Yup from "yup";
import SingleComment from "./SingleComment";
import { useGlobalUserContext } from "../../context/authContext";

const PostView = () => {
  // provide AuthContext
  const { currentUser } = useGlobalUserContext();

  // access id url param
  const { id } = useParams();

  // state for postViewData => posts/:id => null at start
  const [postViewData, setPostViewData] = useState(null);

  // 3 args => initialValues, validationSchema, onSubmit
  const formik = useFormik({
    initialValues: {
      content: "",
    },

    validationSchema: Yup.object({
      content: Yup.string().required("Comment required"),
    }),
    onSubmit: (values, { resetForm }) => {
      console.log(values);

      // create new comment for post
      fetch("/comments", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
          Authorization: `Bearer ${localStorage.getItem("auth_token")}`,
        },
        body: JSON.stringify({
          ...values,
          post_id: id,
        }),
      })
        .then((response) => {
          if (response.ok) {
            alert("Comment created successfully");
            return response.json();
          }
        })
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  });

  // run useEffect everytime id changes
  useEffect(() => {
    // fetch API - 1
    fetch(`/posts/${id}`)
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
      })
      .then((data) => {
        console.log(data);
        setPostViewData(data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, [id]);

  return (
    <div className="pv-container">
      {postViewData ? (
        <div className="pv">
          {/* DISPLAY FLEX */}
          <div className="pv-post-owner">
            <h4>{postViewData.user.full_name}</h4>
            <p>Phase: {postViewData.phase}</p>
          </div>

          <div className="pv-title">
            <h3>{postViewData.title}</h3>
          </div>

          <div className="pv-post-content">{postViewData.content}</div>

          <div className="pv-post-bottom">
            <div className="pv-vote-details">
              <ThumbUpIcon
                onClick={() => {
                  fetch("/votes", {
                    method: "POST",
                    headers: {
                      "Content-Type": "application/json",
                      // Authorization: `Bearer ${currentUser.auth_token}`,
                      Authorization: `Bearer ${localStorage.getItem(
                        "auth_token"
                      )}`,
                      Accept: "application/json",
                    },
                    body: JSON.stringify({
                      vote_type: 1,
                      post_id: id,
                      // user_id: currentUser.data.id, //already passed on the server side
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
              {/* <span>{numberOfVotes.length}</span> */}
              <ThumbDownIcon />
            </div>
            <div className="pv-comment-details">
              <CommentIcon />
              {/* <span>{comments.length}</span> */}
            </div>
          </div>

          <form
            action=""
            className="pv-comment-form"
            onSubmit={formik.handleSubmit}
          >
            <label className="comment-label" htmlFor="">
              Comment as{" "}
              <span className="pv-username">{currentUser.data.username}</span>
            </label>
            <textarea
              id="content"
              name="content"
              value={formik.values.content}
              onChange={formik.handleChange}
              cols="30"
              rows="10"
              className="comment-container"
              placeholder="What are your  thoughts?"
            ></textarea>

            <button type="submit" className="pv-comment-btn">Comment</button>
          </form>

          <div className="comments-container">
            {postViewData.comments &&
              postViewData.comments.map((comment) => {
                return (
                  <SingleComment
                    key={comment.id}
                    {...comment}
                    username={postViewData.user.username}
                  />
                );
              })}
          </div>
        </div>
      ) : (
        <h2>Loading...</h2>
      )}
    </div>
  );
};

export default PostView;
