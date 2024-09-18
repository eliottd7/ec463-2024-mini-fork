const { join } = require('node:path');

const express = require('express');
const app = express();
const { createServer } = require('node:http');
const server = createServer(app);

const IO = require('socket.io');
const picoip = "172.31.36.49"; // server is now turned off so I don't have to pay for it

app.get('/', (req, res) => {
  io.on('connection', (socket) => {
    var clientip = socket.request.connection.remoteAddress;
    if (clientip === picoip) {
      io.emit('pulldata');
    } else {
      res.sendFile(join(__dirname, 'index.html'));
    }
    socket.on('push', (msg) => {
      const parts = msg.split(':'); // should be 3 long...
      io.emit('update_min', parts[0]);
      io.emit('update_max', parts[1]);
      io.emit('update_avg', parts[2]);
    });
  });
});

server.listen(3000, () => {
  console.log('server running at http://localhost:3000');
});
