# Simple Flask webserver to redirect traffic
# This will bounce HTTP requests to a webserver on another port
import sys
from flask import Flask, redirect
app = Flask(__name__)

# Set listening host and port, modify as needed
host, port = '0.0.0.0', 80

# Die and return a usage message if run without a host
usage = "Usage: redirect.py <address>\n"
usage += "Example: redirect.py http://www.google.com"
length = len(sys.argv)
if length < 2:
    sys.exit(usage)
else:
    destination = sys.argv[1]

# Catch traffic on any path
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def bounce(path=''):
    return redirect(destination)

# Instantiate server
if __name__ == "__main__":
    app.run(host=host, port=port, debug=False)