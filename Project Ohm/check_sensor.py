import requests
import json
import os
import time
from datetime import datetime

# ===== LINE OA API =====
LINE_CHANNEL_ACCESS_TOKEN = "NsoqBLYmRJDpTmtCgQ4Ljim8Ehx5FyNzbxPkz4KKTSnxeybs7DL3c4Kzd9ONOcDFROgKbzFVQ7AhOMAistDFE8LUEp6qPTuw4B/56FGQeXCEydc8PHf9KRqMSoYS6Sac7LGiMII0QMqjVvziRXI/MQdB04t89/1O/w1cDnyilFU="
LINE_API_BROADCAST = "https://api.line.me/v2/bot/message/broadcast"

def send_line_alert(message):
    headers = {
        "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messages": [{"type": "text", "text": message}]
    }
    response = requests.post(LINE_API_BROADCAST, headers=headers, json=payload)
    print(f"📤 LINE sent ({response.status_code}) - {message}")

# ===== Load rooms from rooms.json =====
with open("rooms.json", "r", encoding="utf-8") as f:
    rooms = json.load(f)

# ===== Initial room status =====
room_status = {name: True for name in rooms}

# ===== Check every 60 seconds =====
while True:
    for name, info in rooms.items():
        ip = info["ip"]
        print(f"🔍 Checking {name} at {ip}...")

        response = os.system(f"ping -n 1 -w 1000 {ip} >nul")
        is_online = (response == 0)

        if not is_online and room_status[name]:
            message = f"📡 {name} ({ip}) อินเทอร์เน็ตขัดข้อง ❌\nเวลา: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            send_line_alert(message)
            room_status[name] = False

        elif is_online and not room_status[name]:
            message = f"✅ {name} ({ip}) กลับมาออนไลน์แล้ว\nเวลา: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            send_line_alert(message)
            room_status[name] = True

    print("⏳ Waiting 60 seconds...\n")
    time.sleep(60)
