from flask import Flask, jsonify, request
import hashlib

app = Flask(__name__)

def gen_encrypted_key(id):
    return hashlib.sha256(str(id).encode()).hexdigest()

@app.route("/")
def home():
    return "Hello from Dockerized Flask!"
    
@app.route("/status")
def status():
    return jsonify({"status": "running", "container": "flask-app"})

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"

@app.route("/data")
def data():
    id_param = request.args.get('id', '1')
    sample_data = {
        "id": int(id_param),
        "key": gen_encrypted_key(id_param)
    }
    return jsonify(sample_data) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)