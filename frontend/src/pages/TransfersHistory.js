import React, { useEffect, useState } from "react";
import axios from "axios";
import Header from "../components/Header";
import Navbar from "../components/Navbar";
import ClubsBar from "../components/ClubsBar";
import Footer from "../components/Footer";

const leagues = [
    "allsvenskan",
    "bundesliga",
    "eliteserien",
    "eredivisie",
    "jupiler-pro-league",
    "la-liga",
    "liga-nos",
    "ligue-1",
    "premier-league",
    "serie-a",
    "super-league",
    "super-lig",
    "superliga"
]

const formattedDate = (date) => { return new Date(date).toLocaleDateString( "en-US", { weekday: "long", year: "numeric", month: "long", day: "numeric", } ); }


function TransfersHistory() {
  const [TransfersHistory, setTransfersHistory] = useState([]);
  const [selectedLeague, setSelectedLeague] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {

    if (!selectedLeague) return;

    setLoading(true);

    axios.get(`http://localhost:5000/api/football-api/getTransfersHistory/${selectedLeague}`)
    .then(response => {
      setTransfersHistory(response.data);
    })
    .catch(err => console.error(err))
    .finally(() => setLoading(false));
}, [selectedLeague]);

  return (
    <>
      <Header />
      <Navbar />
      <ClubsBar />

      <h3 className="datatype-style" style={{margin: "20px 30px 10px 30px"}} >Top 5 Leagues Transfers History List</h3>

      <div className="btn-group" style={{margin: "10px 30px 50px 30px"}}>
        <button type="button" className="btn btn-danger datatype-style">Choose the League from the Dropdown Menu</button>
        <button type="button" className="btn btn-danger dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
            <span className="visually-hidden">Toggle Dropdown</span>
        </button>
        <ul className="dropdown-menu">
            {leagues.map((league, index) => (
                <li key={index}>
                    <a className="dropdown-item datatype-style" onClick={() => setSelectedLeague(league)}>{league}</a>
                </li>
            ))}
        </ul>
      </div>

      {loading ? (
        <div style={{width: "90%", marginBottom: "50px"}} class="d-flex align-items-center">
            <h5 style={{marginLeft: "100px"}} className="datatype-style" role="status">Loading ... Please Wait !</h5>
            <div class="spinner-border ms-auto" aria-hidden="true"></div>
        </div>
        ) : (

      TransfersHistory.map(p => (
        <div key={p._id} class="card mb-3" style={{width: "95%"}}>
            <div class="row g-0">
                <div class="col-md-4">
                <img src="/images/shoot.png" class="img-fluid rounded-start" alt="player image" style={{width: "60%", height: "100%", border: "2px solid crimson"}} />
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title datatype-style"><span style={{color: "crimson"}}>Player: </span>{p.player}</h5>
                        <h5 class="card-title datatype-style" style={{color: "crimson"}}>Transfers History:</h5>
                        {/* <table className="table-auto rumours-table">
                            <thead>
                                <tr>
                                    <th style={{ color: "pink" }}>Date</th>
                                    <th style={{ color: "pink" }}>Transfer Type</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr key={p._id}>
                                    <td className="datatype-style">{formattedDate(p.transfers.date)}</td>
                                    <td className="datatype-style">{p.transfers.type}</td>
                                </tr>
                                <tr key={p._id}>
                                    <td className="datatype-style">From</td>
                                    <td className="datatype-style">
                                        <img src={p.transfers.teams.out.logo} class="img-fluid rounded-start" alt="club image" style={{width: "20%", height: "20%", border: "2px solid crimson"}} />
                                        {p.transfers.teams.out.name}
                                    </td>
                                </tr>
                                <tr key={p._id}>
                                    <td className="datatype-style">To</td>
                                    <td className="datatype-style">
                                        <img src={p.transfers.teams.in.logo} class="img-fluid rounded-start" alt="club image" style={{width: "20%", height: "20%", border: "2px solid crimson"}} />
                                        {p.transfers.teams.in.name}
                                    </td>
                                </tr>
                            </tbody>
                        </table> */}
                        <div>
                            <button type="button" class="datatype-style btn btn-outline-primary">
                                Date: {formattedDate(p.transfers.date)}
                            </button>
                            <button type="button" style={{marginLeft: "20px"}} class="datatype-style btn btn-outline-primary">
                                Transfer Type: {p.transfers.type}
                            </button>
                            <hr />
                            <div class="transfers-club-container">
                                <img src={p.transfers.teams.out.logo} class="img-fluid rounded-start" alt="club image" style={{width: "6%", height: "6%", border: "2px solid crimson", borderRadius: "5px"}} />
                                <button type="button" class="datatype-style btn btn-outline-danger">
                                    From Club: {p.transfers.teams.out.name}
                                </button>
                            </div>
                            <div class="transfers-club-container">
                                <img src={p.transfers.teams.in.logo} class="img-fluid rounded-start" alt="club image" style={{width: "6%", height: "6%", border: "2px solid green", borderRadius: "5px"}} />
                                <button type="button" style={{marginLeft: "20px"}}  class="datatype-style btn btn-outline-success">
                                    To Club: {p.transfers.teams.in.name}
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
      ))
      )}

        {(TransfersHistory.length == 0) ? 
            <div class="d-grid gap-2">
                <button class="btn btn-primary" type="button">
                    <h5 className="datatype-style">No Data Available Yet ! We Are Still Working On It !</h5>
                </button>
            </div> :
            <div class="d-grid gap-2">
                <button className="btn btn-primary datatype-style" type="button">
                    <h5>Data Are Available and Fetched from Good Hands</h5>
                </button>
            </div>
        }

      <Footer />
    </>
  );
}

export default TransfersHistory;