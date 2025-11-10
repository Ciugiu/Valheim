from fastapi import FastAPI, Request
from threading import Thread
import telebot
import requests
import subprocess
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

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
        subprocess.run(["docker", "compose", "up", "-d"], cwd=VALHEIM_DIR)
        return {"status": "Valheim sever started"}
    elif action == "stop":
        subprocess.run(["docker", "compose", "down"], cwd=VALHEIM_DIR)
        return {"status": "Valheim server stopped"}
    elif action == "status":
        result = subprocess.run(["docker", "compose", "ps", "--status=running"],
                       cwd=VALHEIM_DIR,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       text=True
                       )
        if "Valheim" in result.stdout:
            return {"status": "Server running"}
        else:
            return {"status": "Server stopped"}
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
    bot.polling()

if __name__ == "__main__":
    Thread(target=run_fastapi).start()
    run_bot()

