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


function PlayersList() {
  const [playersList, setPlayersList] = useState([]);
  const [selectedLeague, setSelectedLeague] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {

    if (!selectedLeague) return;

    setLoading(true);

    axios.get(`http://localhost:5000/api/transfermarkt/getPlayersList/${selectedLeague}`)
    .then(response => {
      setPlayersList(response.data);
    })
    .catch(err => console.error(err))
    .finally(() => setLoading(false));
}, [selectedLeague]);

  return (
    <>
      <Header />
      <Navbar />
      <ClubsBar />

      <h3 className="datatype-style" style={{margin: "20px 30px 10px 30px"}} >Top 5 Leagues Players List</h3>

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

      playersList.map(p => (
        <div key={p._id} class="card mb-3" style={{width: "95%"}}>
            <div class="row g-0">
                <div class="col-md-4">
                <img src={p.basic_details.player_image_url} class="img-fluid rounded-start" alt="player image" style={{width: "70%", height: "100%", border: "2px solid crimson"}} />
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title datatype-style"><span style={{color: "crimson"}}>Player Name: </span>{p.basic_details.player_name}</h5>
                        <h5 class="card-title datatype-style"><span style={{color: "crimson"}}>Player Club: </span>{p.basic_details.player_club}</h5>
                        <h5 class="card-title datatype-style"><span style={{color: "crimson"}}>Player Market Value: </span>{p.basic_details.player_market_value}</h5>
                        <h5 class="card-title datatype-style"><span style={{color: "crimson"}}>Player Position: </span>{p.basic_details.player_position}</h5>
                        <h5 class="card-title datatype-style" style={{color: "crimson"}}>Rumours Mill:</h5>
                        {!p.rumours || p.rumours.length === 0 ? (
                        <div className="alert alert-warning datatype-style" role="alert">
                            <h5>No rumours for {p.basic_details.player_name} yet !</h5>
                        </div>
                        ) : (
                        <table className="table-auto rumours-table">
                            <thead>
                                <tr>
                                    <th style={{ color: "pink" }}>Club</th>
                                    <th style={{ color: "pink" }}>Competition</th>
                                </tr>
                            </thead>
                            <tbody>
                                {p.rumours.map((rumour) => (
                                <tr key={p._id}>
                                    <td className="datatype-style">{rumour.club}</td>
                                    <td className="datatype-style">{rumour.competition}</td>
                                </tr>
                                ))}
                            </tbody>
                        </table>
                        )}
                    </div>
                </div>
            </div>
        </div>
      ))
      )}

        {(playersList.length == 0) ? 
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

export default PlayersList;
