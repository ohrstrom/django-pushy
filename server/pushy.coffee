debug = require("debug")("pushy")  if process.env.DEBUG

config = require("./config.json")
io = require("socket.io").listen(config.port)
redis = require("redis").createClient()

redis.psubscribe config.pattern

io.sockets.on "connection", (socket) ->
  debug "socket connection"

  redis
  .on("pmessage", (pattern, channel, data) ->
    data = JSON.parse(data)
    debug "channel", channel
    debug "data", data
    socket.emit "push", data
  )
  .on "error", (err) ->
    console.log "Error " + err