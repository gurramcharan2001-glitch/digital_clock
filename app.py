from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Route for homepage
@app.route("/")
def home():
    return render_template("index.html")

# API route to get current time
@app.route("/get-time")
def get_time():
    response = requests.get("http://worldtimeapi.org/api/timezone/Asia/Kolkata")
    data = response.json()

    current_time = data["datetime"]
    return jsonify({"time": current_time})

if __name__ == "__main__":
    app.run(debug=True)
