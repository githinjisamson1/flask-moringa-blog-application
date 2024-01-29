import React, { useEffect } from "react";
import "./postListing.css";
import SinglePost from "./SinglePost";
import { useGlobalContext } from "../../context/postsContext";

const PostListing = () => {
  // provide PostsContext
  const { setPosts, filteredPosts, setFilteredPosts } = useGlobalContext();

  // proxy:http:127.0.0.1:5555
  // fetch API
  const fetchPosts = () => {
    fetch("/posts")
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
      })
      .then((data) => {
        // console.log(data);
        setPosts(data);
        setFilteredPosts(data);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  // run useEffect on initial render/once
  useEffect(() => {
    fetchPosts();
  }, []);

  return (
    <div className="post-listing-container">
      {filteredPosts.map((post) => {
        return <SinglePost key={post.id} {...post} />;
      })}
    </div>
  );
};

export default PostListing;
