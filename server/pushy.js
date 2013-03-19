var config = require('./config.json');
var io = require('socket.io').listen(config.port);
var redis = require('redis').createClient();

redis.psubscribe(config.pattern);


io.sockets.on('connection', function (socket) {

	console.log('connection')

	redis
	.on('pmessage', function(pattern, channel, data) {
		data = JSON.parse(data);
		cosole.log(data);	
		socket.emit('push', data);
	})
	.on("error", function(err) {
        console.log("Error " + err);
    });
	
});

