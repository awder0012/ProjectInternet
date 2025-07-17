from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
DATA_FILE = 'rooms.json'

def load_rooms():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_rooms(rooms):
    with open(DATA_FILE, 'w') as f:
        json.dump(rooms, f, indent=4)

def ping(ip):
    return os.system(f"ping -n 1 {ip} > nul") == 0  # Windows

@app.route('/')
def index():
    rooms = load_rooms()
    statuses = {}
    for room, info in rooms.items():
        ip = info['ip']
        status = "online" if ping(ip) else "offline"
        statuses[room] = {"ip": ip, "gateway": info['gateway'], "status": status}

    return render_template('dashboard.html', statuses=statuses)

@app.route('/add', methods=['POST'])
def add():
    room_name = request.form['room']
    ip = request.form['ip']
    gateway = request.form['gateway']

    rooms = load_rooms()
    rooms[room_name] = {"ip": ip, "gateway": gateway}
    save_rooms(rooms)

    return redirect('/')

@app.route('/delete/<room>')
def delete(room):
    rooms = load_rooms()
    rooms.pop(room, None)
    save_rooms(rooms)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


