const express = require("express");
const router = express.Router();
const Transfer = require("../models/Transfer");

// GET all transfers
router.get("/", async (req, res) => {
  try {
    const transfers = await Transfer.find().sort({ createdAt: -1 });
    res.json(transfers);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// GET one transfer by ID
router.get("/:id", async (req, res) => {
  try {
    const transfer = await Transfer.findById(req.params.id);
    if (!transfer) {
      return res.status(404).json({ message: "Transfer not found" });
    }
    res.json(transfer);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// POST (optional – for testing or n8n)
router.post("/", async (req, res) => {
  try {
    const newTransfer = new Transfer(req.body);
    await newTransfer.save();
    res.status(201).json(newTransfer);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

module.exports = router;
