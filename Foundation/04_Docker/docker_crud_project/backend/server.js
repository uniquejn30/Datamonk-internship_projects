// backend/server.js
const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');
const fs = require('fs');

const app = express();
const port = 3001;

// --- Middleware ---
// Enable CORS for all routes
app.use(cors());
// Parse JSON bodies
app.use(express.json());

// --- Database Setup ---
const dbPath = './db/database.db';
const dbDir = './db';

// Create the directory if it doesn't exist
if (!fs.existsSync(dbDir)) {
    fs.mkdirSync(dbDir);
}

// Connect to SQLite database
const db = new sqlite3.Database(dbPath, (err) => {
    if (err) {
        console.error('Error opening database', err.message);
    } else {
        console.log('Connected to the SQLite database.');
        // Create table if it doesn't exist
        db.run(`CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )`, (err) => {
            if (err) {
                console.error("Error creating table", err.message);
            } else {
                console.log("Items table is ready.");
            }
        });
    }
});


// --- API Routes (CRUD Operations) ---

// GET: Retrieve all items
app.get('/items', (req, res) => {
    const sql = "SELECT * FROM items ORDER BY id";
    db.all(sql, [], (err, rows) => {
        if (err) {
            res.status(500).json({ "error": err.message });
            return;
        }
        res.json({
            "message": "success",
            "data": rows
        });
    });
});

// POST: Create a new item
app.post('/items', (req, res) => {
    const { name } = req.body;
    if (!name) {
        res.status(400).json({ "error": "Name is required" });
        return;
    }
    const sql = 'INSERT INTO items (name) VALUES (?)';
    db.run(sql, [name], function(err) {
        if (err) {
            res.status(500).json({ "error": err.message });
            return;
        }
        res.status(201).json({
            "message": "success",
            "data": { id: this.lastID, name: name }
        });
    });
});

// PUT: Update an existing item
app.put('/items/:id', (req, res) => {
    const { name } = req.body;
    const { id } = req.params;
    if (!name) {
        res.status(400).json({ "error": "Name is required" });
        return;
    }
    const sql = 'UPDATE items SET name = ? WHERE id = ?';
    db.run(sql, [name, id], function(err) {
        if (err) {
            res.status(500).json({ "error": err.message });
            return;
        }
        if (this.changes === 0) {
            res.status(404).json({ "error": `Item with id ${id} not found` });
            return;
        }
        res.json({
            "message": `Successfully updated item ${id}`,
            "data": { id: id, name: name },
            "changes": this.changes
        });
    });
});

// DELETE: Remove an item
app.delete('/items/:id', (req, res) => {
    const { id } = req.params;
    const sql = 'DELETE FROM items WHERE id = ?';
    db.run(sql, id, function(err) {
        if (err) {
            res.status(500).json({ "error": err.message });
            return;
        }
        if (this.changes === 0) {
            res.status(404).json({ "error": `Item with id ${id} not found` });
            return;
        }
        res.json({
            "message": `Successfully deleted item ${id}`,
            "changes": this.changes
        });
    });
});


// --- Start Server ---
app.listen(port, () => {
    console.log(`Backend server running on http://localhost:${port}`);
});
