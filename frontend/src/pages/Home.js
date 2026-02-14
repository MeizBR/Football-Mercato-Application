import React, { useEffect, useState } from "react";
import Header from "../components/Header";
import Navbar from "../components/Navbar";
import ClubsBar from "../components/ClubsBar";
import TransferCard from "../components/TransferCard";
import Footer from "../components/Footer";
import { fetchTransfers } from "../services/api";

function Home() {
  const [transfers, setTransfers] = useState([]);

  useEffect(() => {
    fetchTransfers()
      .then(res => setTransfers(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <>
      <Header />
      <Navbar />
      <ClubsBar />

      <main className="cards-grid">
        {transfers.map(t => (
          <TransferCard key={t._id} transfer={t} />
        ))}
      </main>

      <Footer />
    </>
  );
}

export default Home;
