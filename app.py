from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Simulated smart home data
home_data = {
    "temperature": 0,
    "humidity": 0,
    "light": 0,
    "door": "Closed",
    "smoke": "No",
    "motion": "Not Detected",
    "ac": "Off",
    "light_status": "Off"
}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/data')
def get_data():
    return jsonify(home_data)

@app.route('/api/update', methods=['POST'])
def update_data():
    global home_data
    home_data.update(request.json)
    return jsonify({"message": "Data received"})

if __name__ == '__main__':
    app.run(debug=True)
