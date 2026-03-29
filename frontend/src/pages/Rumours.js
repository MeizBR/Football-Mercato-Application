import React, { useEffect, useState } from "react";
import Header from "../components/Header";
import Navbar from "../components/Navbar";
import ClubsBar from "../components/ClubsBar";
import Footer from "../components/Footer";
import { fetchLatestRumours } from "../services/fetchRumours";
import RumourCard from "../components/rumoursComponents/rumourCard";

function Rumours() {
  const [rumours, setRumours] = useState([]);

  useEffect(() => {
    fetchLatestRumours()
      .then(res => setRumours(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <>
      <Header />
      <Navbar />
      <ClubsBar />

      <main>
        {rumours.map(r => (
          <RumourCard key={r._id} rumour={r} />
        ))}
      </main>

      <Footer />
    </>
  );
}

export default Rumours;
