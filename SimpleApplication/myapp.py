from flask import Flask
from redis import Redis, RedisError
import os
import socket
import time

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def mainpage():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>no redis available</i>"
    ltime = time.asctime(time.localtime(time.time()))
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
		   "<b>OS:</b> {system} <br/>"\
           "<b>Visits:</b> {visits}<br/>" \
		   "<b>Local Time:</b> {time}"
    return html.format(name=os.getenv("NAME", "world"),system=os.getenv("OS", "Not Windows"), hostname=socket.gethostname(), visits=visits, time=ltime)
	
@app.route("/reset")
def resetCounter():
    try:
        value = redis.getset("counter", 0)
        return "Reset Done"
    except RedisError:
        value = "Reset not possible"
	
    return value

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)