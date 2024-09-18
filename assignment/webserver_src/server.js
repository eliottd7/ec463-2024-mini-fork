const { join } = require('node:path');

const express = require('express');
const app = express();
const { createServer } = require('node:http');
const server = createServer(app);

const IO = require('socket.io');

app.get('/', (req, res) => {
  res.sendFile(join(__dirname, 'index.html'));
});

server.listen(3000, () => {
  console.log('server running at http://localhost:3000');
});

io.on('connection', (socket) => {
  console.log('a user connected');
  socket.on('disconnect', () => {
    console.log('user disconnected');
  });
});
