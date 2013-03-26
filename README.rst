django-pushy - a socket-gateway!
================================

**this package is work in progress - code and documentation are not ready yet!**

Summary
=======

django-pushy is a fast and easy to use solution to enable push support for django-models.

Use case:
---------

- whenever data on a model changes (on save) it's representation in the website(s) should update as well.
 
Technical implementation:
-------------------------

- subscription (callback-function) to pushy-updates (in JavaScript)
- pushy connects to the configured models post-save signal
- on post-save, pushy sends a message to redis
- node.js listens on a configured redis-channel
- node.js sends received updates to the clients
- on update, pushy calls the callback-function in clients browser





Installation
============

.. code-block:: pycon

    pip install -e https://github.com/ohrstrom/django-pushy.git#egg=django-pushy
    
The gateway itself is written in JavaScript, using node.js and socket.io

.. code-block:: pycon

    git clone https://github.com/ohrstrom/django-pushy.git
    cd django-pushy/server/
    npm install
    node pushy.js
    
    
    
Configuration
=============

django
------

In your settings.py add 'pushy' to 'INSTALLED_APPS' and configure the models pushy should monitor for changes - and the hosts in use:

.. code-block:: pycon

	PUSHY_SETTINGS = {
	    'MODELS': (
	               'photosession.session',
	               'photosession.shot',
	               ),
	    'SOCKET_SERVER': 'http://localhost:8888/',
	    'CHANNEL_PREFIX': 'pushy_',
	    'DEBUG': DEBUG
	}


node.js
-------

In django pushy/server/config.json

.. code-block:: json

	{
	    "port" : 8888,
	    "pattern" : "pushy_*"
	}
	
	
Usage
=====

Include the pushy scripts
-------------------------

In order to use django-pushy you have to inlude it's JavaScript part:

.. code-block:: html

   {% load pushy_tags %}
   
   ...
   
   {% pushy_scripts %}
   
   This will render something like:
   
   	<script src="http://localhost:8888/socket.io/socket.io.js"></script>
   	<script type="text/javascript" src="/static/pushy/js/pushy.js"></script>
   	<script>
   		pushy = new PushyApp;
   		pushy.socket_url = 'http://localhost:8888/';
   		pushy.debug = true;
   		pushy.init();
   	</script>




Register for pushy-updates
--------------------------

Imagine you have something like:

.. code-block:: javascript

   var MyApp = function() {
   
   	var self = this;
   	this.api_url;
   	
   	self.init = function() {
   		pushy.subscribe(self.api_url, function() {
   			self.load();
   		});
   		self.load();
   	};
   	
   	this.load = function() {
   
   		$.get(url, function(data) {
   			self.local_data = data;
   			self.displayFunction(data);
   		});
   	};
   	
   	...








