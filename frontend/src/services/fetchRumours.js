import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:5000/api",
});

export const fetchLatestRumours = () => API.get("/transfermarkt/getLatestRumours");
