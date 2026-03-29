import React from "react";

function Header() {
  return (
    <header className="header">
      <nav className="navbar navbar-expand-lg bg-body-tertiary">
        <div className="container-fluid">
          <img src="/images/football.png" alt="Logo" width={40} height={40} style={{marginRight: "15px", border: "5px solid crimson", padding: "2px", borderRadius: "10px"}}/>
          <span className="navbar-brand datatype-style" href="#" style={{color: "crimson"}}>Meirizio Football Mercato</span>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse">
            <span className="navbar-text playwrite-nz-basic">
              Instant Football News, Transfers, and Updates at Your Fingertips
            </span>
          </div>
          <div className="collapse navbar-collapse" id="navbar-logos">
            <img src="/images/tunisia flag.png" alt="Logo" width={40} height={40} style={{marginRight: "15px"}}/>
            <img src="/images/7.png" alt="Logo" width={40} height={40} style={{marginRight: "15px"}}/>
            <img src="/images/10.png" alt="Logo" width={40} height={40} style={{marginRight: "15px"}}/>
            <img src="/images/right-and-left.png" alt="Logo" width={40} height={40} style={{marginRight: "15px"}}/>
            <img src="/images/reporter.png" alt="Logo" width={40} height={40} style={{marginRight: "15px"}}/>
            <img src="/images/analytics.png" alt="Logo" width={40} height={40} style={{marginRight: "15px"}}/>
          </div>
        </div>
      </nav>

      <div>
        <img className="hero-image" src="/images/meirizio.png" alt="Logo" width={1200} height={500}/>
      </div>
    </header>
  );
}

export default Header;
