const mongoose = require("mongoose");

const host = process.env.MONGODB_HOST;
const database = process.env.MONGODB_DATABASE;
const user = process.env.MONGODB_USER;
const password = process.env.MONGODB_PASSWORD;

const connectDB = async () => {
  try {
    await mongoose.connect(
      `mongodb+srv://${user}:${password}@${host}/${database}?retryWrites=true&w=majority`
    );
    console.log("✅ MongoDB connected");
  } catch (error) {
    console.error("❌ MongoDB connection error:", error.message);
    process.exit(1);
  }
};

module.exports = connectDB;
