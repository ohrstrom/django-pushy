PushyApp = function() {

	var self = this;

	this.socket_url = 'http://localhost:8888/';
	this.socket;
	this.debug = true;
	this.subscriptions = [];

	this.init = function() {
		
		setTimeout(function(){
			self.connect()
		}, 100);
	};
	
	this.connect = function() {

		try {
			
			self.socket = io.connect(self.socket_url);
			self.socket.on('push', function(data) {

				if(data.type == 'update') {
					if(self.debug){
						console.log('update for:', data.route);
					}
					self.trigger(data.route);
				};

			});

		} catch(err) {
			console.log(err.message);
		}
	};
	
	this.subscribe = function(route, callback) {
		this.subscriptions.push({
			route: route,
			callback: callback
		});
	};
	
	this.trigger = function(route) {
		for(i in self.subscriptions) {
			if(self.subscriptions[i].route == route) {
				self.subscriptions[i].callback();
			}
		};
	};

	this.bindings = function() {

	};
}; 	