import React, { useEffect, useState } from "react";
import "./postListing.css";
import SinglePost from "./SinglePost";
import { useGlobalContext } from "../../context/postsContext";
import CircularProgress from "@mui/material/CircularProgress";
import Box from "@mui/material/Box";

const PostListing = () => {
  const { posts, setPosts, filteredPosts, setFilteredPosts } =
    useGlobalContext();

  // const [loading, setLoading] = useState(false);

  // proxy:http:127.0.0.1:5555
  // fetch API
  const fetchPosts = () => {
    // setTimeout(() => {
    //   setLoading(!loading);
    // }, 100);

    fetch("/posts")
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        // console.log(data);

        setPosts(data);
        setFilteredPosts(data);

        // setLoading(!loading);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  // run side effect on initial render/once
  useEffect(() => {
    fetchPosts();
  }, []);

  // if (loading) {
  //   return (
  //     <Box sx={{ display: "flex" }}>
  //       <CircularProgress />
  //     </Box>
  //   );
  // }

  return (
    <div className="post-listing-container">
      {filteredPosts.map((post) => {
        return <SinglePost key={post.id} {...post} />;
      })}
    </div>
  );
};

export default PostListing;
