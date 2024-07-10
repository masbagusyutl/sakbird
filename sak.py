import requests
import json
import time
from datetime import datetime, timedelta

# Fungsi untuk mengirimkan permintaan POST
def send_request(telegram_id):
    url = "https://sackbird-backend.liukundavid.workers.dev/api/users/batch/pray"
    payload = {
        "telegramId": telegram_id,
        "totalPrayCoinSum": 200,
        "consumePower": 20,
        "prayEventList": [
            1720577444846,
            1720577446365
        ]
    }
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.status_code

# Membaca data telegramId dari file data.txt
def read_telegram_ids(file_path):
    with open(file_path, 'r') as file:
        telegram_ids = [line.strip() for line in file.readlines()]
    return telegram_ids

# Fungsi untuk menampilkan hitung mundur
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timeformat = f'{hours:02d}:{mins:02d}:{secs:02d}'
        print(f'Next run in: {timeformat}', end='\r')
        time.sleep(1)
        t -= 1

# Fungsi utama untuk mengelola permintaan
def main():
    telegram_ids = read_telegram_ids('data.txt')
    total_accounts = len(telegram_ids)
    
    while True:
        for i, telegram_id in enumerate(telegram_ids):
            print(f"Sending request for account {i+1}/{total_accounts}, ID: {telegram_id}")
            for _ in range(14):
                status_code = send_request(telegram_id)
                print(f"Request status code: {status_code}")
                time.sleep(5)  # Jeda 5 detik antar permintaan
            print(f"Completed 14 requests for account ID: {telegram_id}")
        
        next_run_seconds = 6 * 3600  # 6 jam dalam detik
        countdown(next_run_seconds)

if __name__ == "__main__":
    main()
