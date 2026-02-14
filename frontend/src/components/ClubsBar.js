import React from "react";

function ClubsBar() {
  return (
    <div className="clubs-bar">
      {/* logos empty on purpose */}
      {/* {Array.from({ length: 18 }).map((_, i) => (
        <div key={i} className="club-logo">LOGO</div>
      ))} */}
      <img src="/images/clubs.png" alt="Clubs" width={1150} height={300} />
    </div>
  );
}

export default ClubsBar;
