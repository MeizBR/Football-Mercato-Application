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

      {loading ? (
        <>
            <span class="placeholder col-12"></span>
            <span class="placeholder col-12 bg-primary"></span>
            <span class="placeholder col-12 bg-secondary"></span>
            <span class="placeholder col-12 bg-success"></span>
            <span class="placeholder col-12 bg-danger"></span>
            <span class="placeholder col-12 bg-warning"></span>
            <span class="placeholder col-12 bg-info"></span>
            <span class="placeholder col-12 bg-light"></span>
            <span class="placeholder col-12 bg-dark"></span>
        </>
        ) : (

      playersList.map(p => (
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
                        {!p.rumours || p.rumours.length === 0 ? (
                        <div className="alert alert-warning datatype-style" role="alert">
                            <h5>No rumours for {p.basic_details.player_name} yet !</h5>
                        </div>
                        ) : (
                        <table className="table-auto rumours-table">
                            <thead>
                                <tr>
                                    <th style={{ color: "steelblue" }}>Club</th>
                                    <th style={{ color: "steelblue" }}>Competition</th>
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
                        <hr />
                        <table class="table">
                            <thead>
                                <tr>
                                    <th scope="col">Date</th>
                                    <th scope="col">Amount</th>
                                    <th scope="col">Currency</th>
                                </tr>
                            </thead>
                            <tbody class="table-group-divider">
                                {p.market_value_history_details.slice(0, 3).map((m) => (
                                    <tr>
                                        <td scope="row" className="datatype-style">{m.date}</td>
                                        <td scope="row" className="datatype-style">{m.amount}</td>
                                        <td scope="row" className="datatype-style">{m.currency}</td>
                                    </tr>
                                ))
                                }
                            </tbody>
                        </table>
                        <hr />
                        <div id="carouselExampleCaptions" class="carousel slide">
                        <div class="carousel-indicators">
                            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
                            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
                        </div>
                        <div class="carousel-inner">
                            <div class="carousel-item">
                                {
                                p.gallery_images.slice(0, 3).map((i) => (
                                <div class="grid grid-flow-col grid-rows-4 gap-4">
                                    <img class="d-block w-100" src={i.image_url} alt="player-image"></img>
                                    <div class="carousel-caption d-none d-md-block">
                                        <h5 className="datatype-style">{i.image_title}</h5>
                                    </div>
                                </div>
                                ))
                                }
                            </div>
                        </div>
                        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Previous</span>
                        </button>
                        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Next</span>
                        </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
      ))
      )}

      <Footer />
    </>
  );
}

export default PlayersList;
