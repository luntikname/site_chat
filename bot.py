from flask import Flask, request
from aiogram import Bot
import asyncio

# === ТВОИ ДАННЫЕ ===
TOKEN = "7628649965:AAF2sCiKCK99D_ueDPOSM2refSY65reo6Es"
ADMIN_ID = 960908884

# === НАСТРОЙКА ===
app = Flask(__name__)
bot = Bot(token=TOKEN)

# === ОТПРАВКА ДАННЫХ С САЙТА В ТЕЛЕГРАМ ===
@app.route('/send', methods=['POST'])
def send_data():
    data = request.json
    name = data.get("name")
    service = data.get("service")
    message = data.get("message")

    text = f"📩 Новое сообщение с сайта:\n\n👤 Имя: {name}\n🛠️ Услуга: {service}\n💬 Сообщение: {message}"
    asyncio.run(bot.send_message(ADMIN_ID, text))
    return {"status": "ok"}

if __name__ == "__main__":
    app.run()
