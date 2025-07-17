import requests

channel_access_token = 'lC7hVuLxvQ8XONoj7YbixFRWTKbgXKqxayxjXo6vc9FPeZOwtFHuh/JkKCHVQUDsKBxwg4ZcjXU6BGo4ZCdyaVik9uMR83K7nF2EmkI/Wzb9N+BO9n7sWPwh/82JikPa8hs9Qs2wh9uFbhbmZ4ovBAdB04t89/1O/w1cDnyilFU='

user_ids = [
    'U9841899a54f98e96c5befa8852441aef',
    'Ua47777651e997cf6bab9d04f75ca5e9e',
    'Uaa77c8e7001e1a67d0083a974945e00c',
    'U6b8f870faa7dcdfdd7f73489b90a979c',
]

message_text = '🚨 แจ้งเตือน: อินเทอร์เน็ตล่ม!'

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
        print(f"✅ ส่งข้อความเข้า LINE สำเร็จ: {user_id}")
    else:
        print(f"❌ ส่งไม่สำเร็จ: {user_id} - {response.text}")
