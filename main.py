import discord
from discord.ext import commands
import os, asyncio, random, string
from flask import Flask
from threading import Thread

# --- WEB SERVER GIỮ UPTIME ---
app = Flask('')
@app.route('/')
def home(): return "STATUS: FIGHTING"

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- DANH SÁCH CÂU CHỬI ---
MESSAGES = [
    "Bố mày gõ nhanh hơn mày thở! =)))", "Mày tuổi gì đòi cân bố? =)))",
    "Trình độ đến đâu mà gáy ở đây? =)))", "Cút đi cho nước nó trong! =)))",
    "Nhìn lại bản thân đi thằng con trai! =)))", "Gõ nhanh lên xem nào thằng chậm chạp!",
    "Bố mày khóa mồm mày bằng tốc độ ánh sáng!", "Mày cay không con trai? Cay cũng chẳng làm gì được!",
    "Bố mày là nỗi ám ảnh kinh hoàng nhất đời mày!", "Tốc độ của mày là sự sỉ nhục bàn phím! =)))",
    "Im lặng và quỳ xuống trước tốc độ này đi!", "Bố mày đánh gục ý chí mày trong 3 giây!",
    "Tốc độ này sẽ tiễn mày xuống đáy xã hội!", "Mày tuổi tôm đòi cân cả đại dương à? =)))",
    "Bố mày chấp mày dùng cả tool vẫn thua bố!", "Bố mày vô địch, mày vô dụng, quá rõ ràng!",
    "Trình độ thấp thì ngậm miệng cho sang! =)))", "Bố mày là vua phím, mày là rác thải! =)))"
]

# --- CẤU HÌNH SELF-BOT ---
client = discord.Client()

async def raid_engine():
    await client.wait_until_ready()
    
    # Ép kiểu ID thật chuẩn
    try:
        channel_id = int(os.getenv('CHANNEL_ID').strip())
        target_id = os.getenv('TARGET_USER_ID').strip()
    except Exception as e:
        print(f"LOI CAU HINH ID: {e}")
        return

    channel = client.get_channel(channel_id)
    
    if not channel:
        # Nếu không tìm thấy kênh bằng cache, thử fetch trực tiếp
        try:
            channel = await client.fetch_channel(channel_id)
        except:
            print("KHONG TIM THAY KENH! Kiem tra quyen han acc hoac ID.")
            return

    print(f"MUCH TIEU DA TRONG TAM NGAM: {channel.name}")
    
    while not client.is_closed():
        try:
            msg = random.choice(MESSAGES)
            # Tạo chuỗi random để né bộ lọc trùng lặp của Discord
            rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
            
            # GUI TIN NHAN
            await channel.send(f"<@{target_id}> {msg} | `{rand_str}`")
            
            # TOC DO 0.3S
            await asyncio.sleep(0.3)
            
        except discord.errors.HTTPException as e:
            if e.status == 429: # Rate limit
                print(f"Discord chan tam thoi, nghi {e.retry_after}s")
                await asyncio.sleep(e.retry_after)
            else:
                print(f"Loi HTTP: {e.status}")
                await asyncio.sleep(1)
        except Exception as e:
            print(f"Loi gui tin: {e}")
            await asyncio.sleep(1)

@client.event
async def on_ready():
    print(f"DA THONG HONG CHO ACC: {client.user}")
    client.loop.create_task(raid_engine())

if __name__ == "__main__":
    Thread(target=run).start()
    token = os.getenv('DISCORD_TOKEN').strip()
    # bot=False là bắt buộc cho acc chính
    client.run(token, bot=False)
