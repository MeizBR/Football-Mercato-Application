const mongoose = require("mongoose");

const transferSchema = new mongoose.Schema(
  {
    Date: {
      type: String,
      required: true,
    },
    Title: {
      type: String,
      required: true,
    },
    Content: {
      type: String,
      required: true,
    },
  },
  { timestamps: true }
);

module.exports = mongoose.model("transfers", transferSchema);
