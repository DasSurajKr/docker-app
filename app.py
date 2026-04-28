from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Dockerized Flask!"
    
@app.route("/status")
def status():
    return jsonify({"status": "running", "container": "flask-app"})

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)