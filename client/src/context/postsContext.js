import React, { useEffect, useState, useContext } from "react";

// PostsContext
const PostsContext = React.createContext();

// PostsProvider
const PostsProvider = ({ children }) => {
  // posts + filteredPosts states
  const [posts, setPosts] = useState([]);
  const [filteredPosts, setFilteredPosts] = useState(posts ? posts : []);

  // handle filter posts by phase
  const filterPostByPhase = (phase) => {
    if (phase === "All") {
      setFilteredPosts(posts);
    } else {
      const phasePosts = posts.filter((post) => post.phase === phase);
      setFilteredPosts(phasePosts);
    }
  };

  // wrap return using Provider
  return (
    <PostsContext.Provider
      value={{
        posts,
        setPosts,
        filterPostByPhase,
        filteredPosts,
        setFilteredPosts,
      }}
    >
      {children}
    </PostsContext.Provider>
  );
};

// useGlobalContext can be accessed globally
export const useGlobalContext = () => {
  return useContext(PostsContext);
};

export { PostsContext, PostsProvider };
