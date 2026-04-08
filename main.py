import discord
import os, asyncio, random
from flask import Flask
from threading import Thread

# --- WEB SERVER KIỂM TRA ---
app = Flask('')
@app.route('/')
def home(): return "BOT CHẨN ĐOÁN ĐANG CHẠY"

def run_web():
    app.run(host='0.0.0.0', port=10000)

MESSAGES = ["Vô học!", "Thất học!", "Cút!"]

client = discord.Client()

async def raid_engine():
    print("--- [ST-1] ĐANG CHỜ KẾT NỐI DISCORD... ---")
    await client.wait_until_ready()
    print(f"--- [ST-2] ĐÃ ĐĂNG NHẬP THÀNH CÔNG: {client.user} ---")
    
    # Kiểm tra biến môi trường
    c_id = os.getenv('CHANNEL_ID')
    t_id = os.getenv('TARGET_USER_ID')
    
    if not c_id:
        print("--- [LỖI] THIẾU CHANNEL_ID TRONG TAB ENVIRONMENT! ---")
        return
    if not t_id:
        print("--- [LỖI] THIẾU TARGET_USER_ID TRONG TAB ENVIRONMENT! ---")
        return

    try:
        channel = await client.fetch_channel(int(c_id.strip()))
        print(f"--- [ST-3] ĐÃ TÌM THẤY KÊNH: {channel.name} ---")
        
        while True:
            msg = random.choice(MESSAGES)
            # Tăng delay lên 2.5s như mày muốn
            await channel.send(f"# {msg} \n<@{t_id.strip()}>")
            print(f"-> [OK] Đã vả: {msg}")
            await asyncio.sleep(2.5)
    except Exception as e:
        print(f"--- [LỖI HỆ THỐNG] KHÔNG THỂ GỬI TIN: {e} ---")

@client.event
async def on_ready():
    client.loop.create_task(raid_engine())

if __name__ == "__main__":
    print("--- [START] CODE BẮT ĐẦU CHẠY... ---")
    Thread(target=run_web).start()
    
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print("--- [LỖI] MÀY CHƯA DÁN DISCORD_TOKEN VÀO TAB ENVIRONMENT! ---")
    else:
        print(f"--- [ST-0] ĐANG THỬ ĐĂNG NHẬP VỚI 10 SỐ ĐẦU TOKEN: {token.strip()[:10]}... ---")
        try:
            client.run(token.strip(), bot=False)
        except Exception as e:
            print(f"--- [LỖI] DISCORD TỪ CHỐI LOGIN: {e} ---")
