import React from "react";

const Header = () => {
  return (
    <header className="header">
      <div className="search-bar">
        <input type="text" placeholder="Search..." />
      </div>
      <div className="header-icons">
        <button className="notification-btn">🔔</button>
        <div className="profile-menu">
          <img src="/profile-pic.jpg" alt="Profile" className="profile-pic" />
        </div>
      </div>
    </header>
  );
};

export default Header;
