

# Windows Login Telegram Alerter 🚨

A lightweight Python security script that automatically monitors Windows user authentication and sends an instant notification via Telegram Bot API whenever someone logs into the computer.

## 🛠️ How It Works
1. When a user authenticates/logs into Windows, a trigger is captured.
2. Windows Task Scheduler runs the Python script silently in the background (`pythonw.exe`).
3. The script fetches system details (Hostname, IP, Timestamp) and dispatches a secure alert via Telegram.

## 🚀 Technologies Used
* **Language:** Python 3.13
* **Libraries:** `requests`, `socket`, `time`
* **Windows Tool:** Task Scheduler (Trigger: At Log On)
