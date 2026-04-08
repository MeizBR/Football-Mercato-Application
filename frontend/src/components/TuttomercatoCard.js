import React from "react";

function TuttomercatoCard({ news }) {

  return (
    <div className="card" style={{marginBottom: "20px"}}>
        <div className="card-body">
            <h5 className="datatype-style"><span style={{color: "crimson"}}>Date:</span> {news.date}</h5>
            <h5 className="datatype-style"><span style={{color: "crimson"}}>Content:</span> {news.detail}</h5>
        </div>
    </div>
  );
}

export default TuttomercatoCard;
