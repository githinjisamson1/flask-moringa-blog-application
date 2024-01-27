import React, { useEffect, useState } from "react";
import "./postListing.css";
import SinglePost from "./SinglePost";
import { useGlobalContext } from "../../context/postsContext";

const PostListing = () => {
  const { posts, setPosts, filteredPosts, setFilteredPosts } =
    useGlobalContext();

  //   if (posts) {
  //     setFilteredPosts(posts);
  //   }

  const fetchPosts = () => {
    fetch("/posts")
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        // console.log(data);
        setPosts(data);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  useEffect(() => {
    fetchPosts();
  }, []);

  return (
    <div className="post-listing-container">
      {posts.map((post) => {
        return <SinglePost key={post.id} {...post} />;
      })}
    </div>
  );
};

export default PostListing;