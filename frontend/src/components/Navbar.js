import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">
      <Link to="/" className="datatype-style">Latest News</Link>
      <Link to="/rumours" className="datatype-style">Rumours</Link>
      <a href="/" className="datatype-style">Latest Transfers</a>
      <a href="/" className="datatype-style">Transfers History</a>
      <a href="/" className="datatype-style">Teams</a>
      <Link to="/playersList" className="datatype-style">Players</Link>
      <a href="/" className="datatype-style">Leagues</a>
      <Link to="/tuttomercato" className="datatype-style">Tuttomercato News</Link>
    </nav>
  );
}

export default Navbar;
