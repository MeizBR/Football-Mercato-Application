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
    "laliga",
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

  useEffect(() => {
    console.log("selectedLeague:", selectedLeague);

    if (!selectedLeague) {
        console.log("Blocked API call");
        return;
    }

    console.log("Calling API...");

    axios.get(`http://localhost:5000/api/transfermarkt/getPlayersList/${selectedLeague}`)
      .then(response => {
        setPlayersList(response.data);
      })
      .catch(err => console.error(err));;
  }, [selectedLeague]);

  return (
    <>
      <Header />
      <Navbar />
      <ClubsBar />

      <h3 className="datatype-style" style={{marginTop: "50px"}} >Top 5 Leagues Players List</h3>

      <div className="btn-group" style={{marginBottom: "50px"}}>
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

      {playersList.map(p => (
        <div key={p._id} class="card mb-3" style={{width: "95%"}}>
            <div class="row g-0">
                <div class="col-md-4">
                <img src={p.basic_details.player_image_url} class="img-fluid rounded-start" alt="player image" style={{width: "50%", height: "100%"}} />
                </div>
                <div class="col-md-8">
                <div class="card-body">
                    <h5 class="card-title datatype-style"><span style={{color: "crimson"}}>Player Name: </span>{p.basic_details.player_name}</h5>
                    <h5 class="card-title datatype-style"><span style={{color: "crimson"}}>Player Club: </span>{p.basic_details.player_club}</h5>
                    <h5 class="card-title datatype-style"><span style={{color: "crimson"}}>Player Market Value: </span>{p.basic_details.player_market_value}</h5>
                    <h5 class="card-title datatype-style"><span style={{color: "crimson"}}>Player Position: </span>{p.basic_details.player_position}</h5>
                    <h5 class="card-title datatype-style" style={{color: "crimson"}}>Rumours:</h5>
                    <table class="table-auto rumours-table">
                        <thead>
                            <tr>
                                <th style={{color: "steelblue"}}>Club</th>
                                <th style={{color: "steelblue"}}>Competition</th>
                            </tr>
                        </thead>
                        {(p.rumours).map((rumour) => (
                            <tbody>
                                <tr>
                                    <td class="datatype-style">{rumour.club}</td>
                                    <td class="datatype-style">{rumour.competition}</td>
                                </tr>
                            </tbody>
                        ))}
                    </table>
                </div>
                </div>
            </div>
        </div>
      ))}

      <Footer />
    </>
  );
}

export default PlayersList;
