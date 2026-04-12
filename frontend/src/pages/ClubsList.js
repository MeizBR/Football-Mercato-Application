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


function ClubsList() {
  const [ClubsList, setClubsList] = useState([]);
  const [selectedLeague, setSelectedLeague] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {

    if (!selectedLeague) return;

    setLoading(true);

    axios.get(`http://localhost:5000/api/transfermarkt/getClubsList/${selectedLeague}`)
    .then(response => {
      setClubsList(response.data);
    })
    .catch(err => console.error(err))
    .finally(() => setLoading(false));
}, [selectedLeague]);

  return (
    <>
      <Header />
      <Navbar />
      <ClubsBar />

      <h3 className="datatype-style" style={{margin: "20px 30px 10px 30px"}} >Top 5 Leagues Clubs List</h3>

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
        <div style={{width: "90%", marginBottom: "50px", marginLeft: "100px"}} class="progress" role="progressbar" aria-label="Animated striped example" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
            <div class="progress-bar progress-bar-striped progress-bar-animated" style={{width: "75%"}}></div>
            <div class="progress-bar progress-bar-striped progress-bar-animated" style={{width: "75%"}}></div>
            <div class="progress-bar progress-bar-striped progress-bar-animated" style={{width: "75%"}}></div>
        </div>
        ) : (

      ClubsList.map(p => (
        <div key={p._id} class="card mb-3" style={{width: "95%"}}>
            <div class="row g-0">
                <div class="col-md-4">
                <img src="/images/top-5.webp" class="img-fluid rounded-start" alt="player image" style={{width: "60%", height: "100%", border: "2px solid crimson"}} />
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title datatype-style"><span style={{color: "crimson"}}>Team: </span>{p.club_name}</h5>
                        <hr />
                        <h5 class="card-title datatype-style"><span style={{color: "crimson"}}>˖ ᡣ𐭩 ⊹ ࣪  ౨ৎ˚₊ ¸„.-•~¹°”ˆ˜¨ 𝙛𝙤𝙤𝙩𝙗𝙖𝙡𝙡 ¨˜ˆ”°¹~•-.„¸ ♜🍭  ｍｅιŕ𝓩𝐢𝓞  ♠💚</span></h5>
                    </div>
                </div>
            </div>
        </div>
      ))
      )}

        {(ClubsList.length == 0) ? 
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

export default ClubsList;