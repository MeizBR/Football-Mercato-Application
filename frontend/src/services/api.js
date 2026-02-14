import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:5000/api", // change later
});

export const fetchTransfers = () => API.get("/transfers");
