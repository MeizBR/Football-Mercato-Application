const express = require("express");
require("dotenv").config();

const cors = require("cors");
const connectDB = require("./config/db");
const transferRoutes = require("./routes/transferRoutes");

const app = express();

// middleware
app.use(express.json());
app.use(cors());

// DB connection
connectDB();

// routes
app.get("/", (req, res) => {
  res.json({ status: "API is running 🚀" });
});

app.use("/api/transfers", transferRoutes);

// server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`🚀 Server running on port ${PORT}`);
});
