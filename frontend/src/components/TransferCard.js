import React from "react";

function TransferCard({ transfer }) {
  return (
    <div className="transfer-card">
      <div className="card-image">
        <img src="/images/transfer.png" alt={transfer.Title} width={330} height={200}/>
      </div>
      <hr />
      <div className="card-content">
        <div className="card-title">Date</div>
        <p>{transfer.Date}</p>
        <div className="card-title">Title</div>
        <p>{transfer.Title}</p>
        <div className="card-title">Content</div>
        <p> {transfer.Content}</p>
      </div>
    </div>
  );
}

export default TransferCard;
