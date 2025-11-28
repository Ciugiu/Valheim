from fastapi import FastAPI, Request
from threading import Thread
import telebot
import requests
import subprocess
import uvicorn
import os
import time
import signal
import sys
import docker
from dotenv import load_dotenv

load_dotenv()
client = docker.from_env()

# ============ CONFIG ============
BOT_TOKEN = os.getenv("BOT_TOKEN")
NGROK_URL = os.getenv("NGROK_URL")
VALHEIM_DIR = os.getenv("VALHEIM_DIR")  # path to docker-compose.yml
ALLOWED_IDS = [int(x) for x in os.getenv("ALLOWED_IDS", "").split(",") if x]
# ================================

app = FastAPI()
bot = telebot.TeleBot(BOT_TOKEN)


# ======= FASTAPI ENDPOINT =======
@app.post("/valheim")
async def handle_request(request: Request):
    data = await request.json()

    action = data.get("action")

    if action == "start":
        client.containers.get("Valheim").start()
        return {"status": "Valheim sever started"}
    elif action == "stop":
        client.containers.get("Valheim").stop()
        return {"status": "Valheim server stopped"}
    elif action == "status":
        try:
            container = client.containers.get("Valheim")
            if container.status == "running":
                return {"status": "Server running"}
            else:
                return {"status": "Server stopped"}
        except docker.errors.NotFound:
            return {"status": "Valheim container not found"}
    else:
        return {"status": "unknown action"}


# ===== TELEGRAM BOT HANDLER =====
@bot.message_handler(commands=['start', 'stop', 'status'])
def handle_command(message):
    if message.from_user.id not in ALLOWED_IDS:
        return bot.reply_to(message, "Not authorized.")
    action = message.text.strip('/').lower()
    try:
        resp = requests.post(f"{NGROK_URL}/valheim", json={
            "action": action,
        })
        status = resp.json().get("status", "unknown")
        bot.reply_to(message, f"Server action: {status}")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")


def run_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=8000)

def run_bot():
    while True:
        try:
            bot.polling(non_stop=True, interval=1, timeout=30)
        except Exception as e:
            print("Polling error:", e)
            time.sleep(3)

def handle_sigint(sig, frame):
    print("Shutting down cleanly...")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)


if __name__ == "__main__":
    Thread(target=run_fastapi).start()
    run_bot()

