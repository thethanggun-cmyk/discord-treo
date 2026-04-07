import discord
import os, asyncio, random, string
from flask import Flask
from threading import Thread

# --- WEB SERVER GIỮ UPTIME ---
app = Flask('')
@app.route('/')
def home(): return "DA THONG HONG"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- DANH SÁCH CÂU CHỬI ---
MESSAGES = [
    "Bố mày gõ nhanh hơn mày thở! =)))", "Mày tuổi gì đòi cân bố? =)))",
    "Trình độ đến đâu mà gáy ở đây? =)))", "Cút đi cho nước nó trong! =)))",
    "Bố mày khóa mồm mày bằng tốc độ ánh sáng!", "Mày cay không con trai? Cay cũng chẳng làm gì được!",
    "Bố mày là nỗi ám ảnh kinh hoàng nhất đời mày!", "Tốc độ của mày là sự sỉ nhục bàn phím! =)))",
    "Im lặng và quỳ xuống trước tốc độ này đi!", "Bố mày đánh gục ý chí mày trong 3 giây!",
    "Bố mày là vua phím, mày là rác thải! =)))", "Nhìn lại bản thân đi thằng con trai! =)))"
]

client = discord.Client()

async def raid_engine():
    await client.wait_until_ready()
    print(f"--- DA DANG NHAP ACC: {client.user} ---")
    
    try:
        # Lay ID tu Render, xoa khoang trang
        c_id_raw = os.getenv('CHANNEL_ID', '').strip()
        t_id_raw = os.getenv('TARGET_USER_ID', '').strip()
        
        if not c_id_raw:
            print("!!! CHUA NHAP CHANNEL_ID TRONG TAB ENVIRONMENT !!!")
            return

        c_id = int(c_id_raw)
        channel = await client.fetch_channel(c_id)
        
        print(f"--- DA KET NOI KENH: {channel.name} - BAT DAU VA 0.3S ---")
        
        while True:
            try:
                msg = random.choice(MESSAGES)
                suffix = ''.join(random.choices(string.digits, k=4))
                # GUI TIN NHAN
                await channel.send(f"<@{t_id_raw}> {msg} | `{suffix}`")
                print("-> DA NHẢ CHỮ THANH CONG!")
            except Exception as e:
                print(f"!!! KHONG GUI DUOC VI: {e}")
            
            await asyncio.sleep(0.3)
            
    except Exception as e:
        print(f"!!! LOI ID HOAC KENH: {e}")

@client.event
async def on_ready():
    client.loop.create_task(raid_engine())

if __name__ == "__main__":
    Thread(target=run_web).start()
    token = os.getenv('DISCORD_TOKEN', '').strip()
    # Tu dong thu ca 2 cach chay cho acc chinh
    try:
        client.run(token, bot=False)
    except:
        client.run(token)
