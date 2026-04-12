import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Rumours from "./pages/Rumours"
import PlayersList from "./pages/PlayersList";
import Tuttomercato from "./pages/Tuttomercato";
import TransfersHistory from "./pages/TransfersHistory";
import ClubsList from "./pages/ClubsList";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/rumours" element={<Rumours />} />
        <Route path="/playersList" element={<PlayersList />} />
        <Route path="/tuttomercato" element={<Tuttomercato />} />
        <Route path="/transfersHistory" element={<TransfersHistory />} />
        <Route path="/clubsList" element={<ClubsList />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
