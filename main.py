import discord
import os, asyncio, random, string
from flask import Flask
from threading import Thread

# --- WEB SERVER GIỮ UPTIME ---
app = Flask('')
@app.route('/')
def home(): return "DA THONG HONG - DANG CHIEN"

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- DANH SÁCH CÂU CHỬI ---
MESSAGES = [
    "Bố mày gõ nhanh hơn mày thở! =)))", "Mày tuổi gì đòi cân bố? =)))",
    "Trình độ đến đâu mà gáy ở đây? =)))", "Cút đi cho nước nó trong! =)))",
    "Bố mày khóa mồm mày bằng tốc độ ánh sáng!", "Mày cay không con trai? Cay cũng chẳng làm gì được!",
    "Bố mày là nỗi ám ảnh kinh hoàng nhất đời mày!", "Tốc độ của mày là sự sỉ nhục bàn phím! =)))",
    "Im lặng và quỳ xuống trước tốc độ này đi!", "Bố mày đánh gục ý chí mày trong 3 giây!",
    "Mày tuổi tôm đòi cân cả đại dương à? =)))", "Bố mày là vua phím, mày là rác thải! =)))"
]

client = discord.Client()

async def raid_engine():
    await client.wait_until_ready()
    print(f"--- DA DANG NHAP VAO ACC: {client.user} ---")
    
    try:
        c_id = int(os.getenv('CHANNEL_ID').strip())
        t_id = os.getenv('TARGET_USER_ID').strip()
        channel = await client.fetch_channel(c_id)
        
        print(f"--- DA TIM THAY KENH: {channel.name} ---")
        
        while True:
            try:
                msg = random.choice(MESSAGES)
                suffix = ''.join(random.choices(string.digits, k=4))
                # LENH GUI TIN NHAN
                await channel.send(f"<@{t_id}> {msg} | `{suffix}`")
                print(f"-> DA GUI THANH CONG!")
            except Exception as e:
                print(f"!!! LOI KHI GUI TIN: {e}")
            
            await asyncio.sleep(0.3) # TOC DO 0.3S
            
    except Exception as e:
        print(f"!!! LOI KHOI CHAY RAID: {e}")

@client.event
async def on_ready():
    client.loop.create_task(raid_engine())

if __name__ == "__main__":
    Thread(target=run).start()
    token = os.getenv('DISCORD_TOKEN').strip()
    client.run(token, bot=False)
