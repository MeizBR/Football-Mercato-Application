import React from "react";

function RumourCard({ rumour }) {

  return (
    <ul class="list-group list-group-flush" style={{marginBottom: "25px", border: "2px solid pink"}}>
        <li class="list-group-item datatype-style"><img src="/images/bullet-point.png" alt="club image" width={20} height={20}  style={{marginRight: "10px"}}/><span style={{color: "crimson"}}>Player Name: </span>{rumour.player_name}</li>
        <li class="list-group-item datatype-style"><img src="/images/bullet-point.png" alt="club image" width={20} height={20}  style={{marginRight: "10px"}}/><span style={{color: "crimson"}}>Player Current Club: </span>{rumour.current_club}</li>
        <li class="list-group-item datatype-style"><img src="/images/bullet-point.png" alt="club image" width={20} height={20}  style={{marginRight: "10px"}}/><span style={{color: "crimson"}}>Player Market Value: </span>{rumour.market_value}</li>
        <li class="list-group-item datatype-style"><img src="/images/bullet-point.png" alt="club image" width={20} height={20}  style={{marginRight: "10px"}}/><span style={{color: "crimson"}}>Player Joining Destination: </span>{rumour.joining_destination}</li>
        <li class="list-group-item datatype-style">
            <img src="/images/bullet-point.png" alt="club image" width={20} height={20}  style={{marginRight: "10px"}}/><span style={{color: "crimson"}}>Departure Club: </span>{rumour.departure_club.club_name} <img src={rumour.departure_club.club_image_url} alt="club image" width={40} height={50} style={{marginLeft: "20px", marginRight: "50px"}}/>
            <img src="/images/bullet-point.png" alt="club image" width={20} height={20}  style={{marginRight: "10px"}}/><span style={{color: "crimson"}}>Arrival Club: </span>{rumour.arrival_club.club_name} <img src={rumour.arrival_club.club_image_url} alt="club image" width={40} height={50} style={{marginLeft: "20px"}}/>
        </li>
    </ul>
  );
}

export default RumourCard;
