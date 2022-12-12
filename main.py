from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Define a route for serving the HTML file
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/static/<path:path>")
def serve_static(path):
    return send_from_directory("static", path)
