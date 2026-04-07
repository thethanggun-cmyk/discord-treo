import discord
import os, asyncio, random, string
from flask import Flask
from threading import Thread

# --- WEB SERVER GIỮ UPTIME ---
app = Flask('')
@app.route('/')
def home(): return "DA THONG HONG - DANG CHAY 0.3S"

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- DANH SÁCH CÂU CHỬI GẮT ---
MESSAGES = [
    "Bố mày gõ nhanh hơn mày thở! =)))", "Mày tuổi gì đòi cân bố? =)))",
    "Trình độ đến đâu mà gáy ở đây? =)))", "Cút đi cho nước nó trong! =)))",
    "Nhìn lại bản thân đi thằng con trai! =)))", "Gõ nhanh lên xem nào thằng chậm chạp!",
    "Bố mày khóa mồm mày bằng tốc độ ánh sáng!", "Mày cay không con trai? Cay cũng chẳng làm gì được!",
    "Bố mày là nỗi ám ảnh kinh hoàng nhất đời mày!", "Tốc độ của mày là sự sỉ nhục bàn phím! =)))",
    "Im lặng và quỳ xuống trước tốc độ này đi!", "Bố mày đánh gục ý chí mày trong 3 giây!",
    "Mày tuổi tôm đòi cân cả đại dương à? =)))", "Bố mày chấp mày dùng cả tool vẫn thua bố!",
    "Trình độ thấp thì ngậm miệng cho sang! =)))", "Bố mày là vua phím, mày là rác thải! =)))"
]

client = discord.Client()

async def attack():
    await client.wait_until_ready()
    # Ép kiểu ID kênh và mục tiêu
    c_id = int(os.getenv('CHANNEL_ID').strip())
    t_id = os.getenv('TARGET_USER_ID').strip()
    
    channel = client.get_channel(c_id)
    if not channel:
        try: channel = await client.fetch_channel(c_id)
        except: 
            print("LOI: Khong tim thay kenh!")
            return

    print(f"DANG VA 0.3S VAO KENH: {channel.name}")
    
    while True:
        try:
            m = random.choice(MESSAGES)
            s = ''.join(random.choices(string.digits, k=4))
            # Gui tin nhan
            await channel.send(f"<@{t_id}> {m} | `{s}`")
            await asyncio.sleep(0.3)
        except discord.errors.HTTPException as e:
            if e.status == 429: await asyncio.sleep(e.retry_after)
            else: await asyncio.sleep(1)
        except: await asyncio.sleep(1)

@client.event
async def on_ready():
    print(f"ACC CHINH ONLINE: {client.user}")
    client.loop.create_task(attack())

if __name__ == "__main__":
    Thread(target=run).start()
    token = os.getenv('DISCORD_TOKEN').strip()
    # bot=False bat buoc de acc chinh nhả chữ
    client.run(token, bot=False)
