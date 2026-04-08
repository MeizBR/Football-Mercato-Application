import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Rumours from "./pages/Rumours"
import PlayersList from "./pages/PlayersList";
import Tuttomercato from "./pages/Tuttomercato";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/rumours" element={<Rumours />} />
        <Route path="/playersList" element={<PlayersList />} />
        <Route path="/tuttomercato" element={<Tuttomercato />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
