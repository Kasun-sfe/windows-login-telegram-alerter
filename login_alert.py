import requests
import socket
from datetime import datetime
import time

# මෙතනට ඔයාගේ Bot Token එකයි Chat ID එකයි දාන්න
BOT_TOKEN = "Enter Your API"
CHAT_ID = "Enter Your Chat ID"

def send_telegram_alert():
    # අන්තර්ජාලය connect වෙනකල් තත්පර 10ක් ඉන්නවා
    time.sleep(10) 
    
    # PC එකේ විස්තර ලබාගැනීම
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # යවන Message එක
    message = f"🚨 Laptop Login Alert!\n\n👤 යමෙකු ලැප්ටොප් එකට ලොග් විය.\n💻 Hostname: {hostname}\n🌐 IP: {ip_address}\n🕒 Time: {login_time}"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    
    try:
        requests.post(url, data=data)
    except Exception as e:
        # Internet නැත්නම් error එකක් එන එක නවත්තන්න
        pass

if __name__ == "__main__":
    send_telegram_alert()