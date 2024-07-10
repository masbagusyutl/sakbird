import requests
import json
import time
from datetime import datetime

# Fungsi untuk mengirimkan permintaan POST
def send_request(telegram_id):
    url = "https://sackbird-backend.liukundavid.workers.dev/api/users/batch/pray"
    payload = {
        "telegramId": telegram_id,
        "totalPrayCoinSum": 2000,
        "consumePower": 200
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.status_code

# Membaca data telegramId dari file data.txt
def read_telegram_ids(file_path):
    with open(file_path, 'r') as file:
        telegram_ids = [line.strip() for line in file.readlines()]
    return telegram_ids

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
            print(f"Completed 14 requests for account ID: {telegram_id}")
        print(f"All accounts processed. Next run at: {datetime.now() + timedelta(hours=6)}")
        time.sleep(6 * 3600)  # Tidur selama 6 jam sebelum iterasi berikutnya

if __name__ == "__main__":
    main()
