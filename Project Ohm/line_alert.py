import sys
import requests

channel_access_token = 'NsoqBLYmRJDpTmtCgQ4Ljim8Ehx5FyNzbxPkz4KKTSnxeybs7DL3c4Kzd9ONOcDFROgKbzFVQ7AhOMAistDFE8LUEp6qPTuw4B/56FGQeXCEydc8PHf9KRqMSoYS6Sac7LGiMII0QMqjVvziRXI/MQdB04t89/1O/w1cDnyilFU='

user_ids = [
    'U9841899a54f98e96c5befa8852441aef',
    '',
]

room = sys.argv[1]
message_detail = sys.argv[2]

message_text = f'🚨 แจ้งเตือน: {message_detail}'

url = 'https://api.line.me/v2/bot/message/push'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + channel_access_token
}

for user_id in user_ids:
    data = {
        'to': user_id,
        'messages': [{
            'type': 'text',
            'text': message_text
        }]
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"✅ ส่งแจ้งเตือน {room} สำเร็จ")
    else:
        print(f"❌ แจ้งเตือนไม่สำเร็จ: {response.text}")
