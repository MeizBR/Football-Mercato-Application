import React, { useEffect, useState } from "react";
import Header from "../components/Header";
import Navbar from "../components/Navbar";
import ClubsBar from "../components/ClubsBar";
import Footer from "../components/Footer";
import { fetchLatestTuttomercatoNews } from "../services/fetchTuttomercato";
import TuttomercatoCard from "../components/TuttomercatoCard";

function Tuttomercato() {
  const [tuttomercatoNews, setTuttomercatoNews] = useState([]);

  useEffect(() => {
    fetchLatestTuttomercatoNews()
      .then(res => setTuttomercatoNews(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <>
      <Header />
      <Navbar />
      <ClubsBar />

      <div class="d-grid gap-2 col-6 mx-auto">
        <button  style={{margin: "20px 0"}} className="btn btn-primary datatype-style" type="button">Tuttomercato Latest News Fetched</button>
      </div>

      <main>
        {tuttomercatoNews.map(t => (
          <TuttomercatoCard key={t._id} news={t} />
        ))}
      </main>

      <Footer />
    </>
  );
}

export default Tuttomercato;