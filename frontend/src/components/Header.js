import React from "react";

function Header() {
  return (
    <header className="header">
      <nav className="navbar navbar-expand-lg bg-body-tertiary">
        <div className="container-fluid">
          <img src="/images/football.png" alt="Logo" width={35} height={35} style={{marginRight: "35px"}}/>
          <a className="navbar-brand playwrite-cu-guides-regular" href="#">Meirizio Football Mercato News</a>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarText">
            <span className="navbar-text playwrite-nz-basic">
              Instant Football News, Transfers, and Updates at Your Fingertips
            </span>
          </div>
          <div className="collapse navbar-collapse" id="navbarText">
            <img src="/images/tunisia flag.png" alt="Logo" width={50} height={50} style={{marginRight: "35px"}}/>
            <img src="/images/7.png" alt="Logo" width={50} height={50} style={{marginRight: "35px"}}/>
            <img src="/images/10.png" alt="Logo" width={50} height={50} style={{marginRight: "35px"}}/>
          </div>
        </div>
      </nav>

      <div className="hero">
        <img className="hero-image" src="/images/meirizio.png" alt="Logo" width={1200} height={500}/>
      </div>
    </header>
  );
}

export default Header;
