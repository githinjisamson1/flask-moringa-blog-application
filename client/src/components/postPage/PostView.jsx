import React, { useCallback, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "./postView.css";
import ThumbUpIcon from "@mui/icons-material/ThumbUp";
import ThumbDownIcon from "@mui/icons-material/ThumbDown";
import CommentIcon from "@mui/icons-material/Comment";
import { useFormik } from "formik";
import * as Yup from "yup";
import SingleComment from "./SingleComment";

const PostView = () => {
  // access id url param
  const { id } = useParams();

  const [postViewData, setPostViewData] = useState([]);

  const formik = useFormik({
    initialValues: {
      postComment: "",
    },

    validationSchema: Yup.object({
      postComment: Yup.string().required("Comment required"),
    }),
  });

  // const fetchSinglePost = () => {

  // };

  useEffect(() => {
    // fetchSinglePost()
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
            <h4>Lorem, ipsum dolor.</h4>
            <p>Phase: 1</p>
          </div>

          <div className="pv-title">
            <h3>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae,
              similique?
            </h3>
          </div>

          <div className="pv-post-content">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui ad
            mollitia ab minima amet ipsam laudantium quia, alias nihil neque
            esse cupiditate molestias, voluptatem tempora? Exercitationem facere
            doloribus optio ut dolores, sunt officia veniam a quas unde eius
            porro tempora adipisci maiores quia? Aspernatur nam perspiciatis
            praesentium quas harum quo, cupiditate eligendi dolore at explicabo
            eaque, sit, quasi esse blanditiis doloribus quam nemo vel! Modi qui
            ullam aspernatur id amet dolorem pariatur debitis at eligendi!
          </div>

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

          <form action="" className="pv-comment-form">
            <label className="comment-label" htmlFor="">Comment as <span className="pv-username">Nahason</span></label>
            <textarea
              name=""
              id=""
              cols="30"
              rows="10"
              className="comment-container"
              placeholder="What are your  thoughts?"
            ></textarea>

            <button className="pv-comment-btn">Comment</button>
          </form>

          <div className="comments-container">
            {postViewData.comments &&
              postViewData.comments.map((comment) => {
                return <SingleComment key={comment.id} {...comment} />;
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
