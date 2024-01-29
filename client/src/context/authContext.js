import React, { useContext, useState } from "react";

const UserContext = React.createContext();

const UserProvider = ({ children }) => {
  const [currentUser, setCurrentUser] = useState({});

  return (
    <UserContext.Provider
      value={{
        currentUser,
        setCurrentUser,
      }}
    >
      {children}
    </UserContext.Provider>
  );
};

const useGlobalUserContext = () => {
  return useContext(UserContext);
};

export { UserProvider, useGlobalUserContext };
