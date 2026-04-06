import discord
from discord.ext import commands
import os, asyncio, random, string
from flask import Flask
from threading import Thread

# --- GIỮ UPTIME CHO RENDER ---
app = Flask('')
@app.route('/')
def home(): return "SELF-BOT IS RUNNING"

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- DANH SÁCH CÂU CHỬI ---
MESSAGES = [
    "Bố mày gõ nhanh hơn mày thở! =)))", "Mày tuổi gì đòi cân bố? =)))",
    "Trình độ đến đâu mà gáy ở đây? =)))", "Cút đi cho nước nó trong! =)))",
    "Nhìn lại bản thân đi thằng con trai! =)))", "Gõ nhanh lên xem nào thằng chậm chạp!",
    "Mày đang đấu với một cỗ máy đấy! =)))", "Bố mày khóa mồm mày bằng tốc độ ánh sáng!",
    "Mày cay không con trai? Cay cũng chẳng làm gì được!", "Trình độ mày chỉ đủ để quét rác cho server!",
    "Một lũ vô dụng đang cố chống lại vị vua! =)))", "Bố mày là nỗi ám ảnh kinh hoàng nhất đời mày!",
    "Tốc độ của mày là sự sỉ nhục bàn phím! =)))", "Bố mày đã ấn định kết cục thảm hại! =)))",
    "Im lặng và quỳ xuống trước tốc độ này đi!", "Bố mày đánh gục ý chí mày trong 3 giây!",
    "Mày chỉ là phế vật trong cuộc chiến bàn phím!", "Tốc độ này sẽ tiễn mày xuống đáy xã hội!",
    "Mày tuổi tôm đòi cân cả đại dương à? =)))", "Nhìn dòng này mà cay cú đi con! =)))",
    "Bố mày chấp mày dùng cả tool vẫn thua bố!", "Bố mày vô địch, mày vô dụng, quá rõ ràng!",
    "Mày là minh chứng cho việc tiến hóa ngược!", "Bố mày là cơn ác mộng vĩnh hằng của mày!",
    "Trình độ thấp thì ngậm miệng cho sang! =)))", "Bố mày gõ phím bằng cả tương lai nhà mày!",
    "Nhìn cách mày phản kháng thật tội nghiệp! =)))", "Mày gõ tiếp đi cho thế giới thấy mày kém!",
    "Mày nghĩ mày ngầu nhưng thật ra tấu hài!", "Bố mày là vua phím, mày là rác thải! =)))"
]

# --- CẤU HÌNH SELF-BOT ---
# Lưu ý: Self-bot không dùng bot=True
client = discord.Client()

async def start_raid():
    await client.wait_until_ready()
    c_id = os.getenv('CHANNEL_ID')
    t_id = os.getenv('TARGET_USER_ID')
    channel = client.get_channel(int(c_id))
    
    if channel:
        print(f"SELF-BOT ĐANG VẢ 0.3S TẠI: {c_id}")
        while True:
            try:
                msg = random.choice(MESSAGES)
                # Acc chính gửi nhanh rất dễ bị ăn "Phone Verification" nên kèm số ngẫu nhiên là bắt buộc
                suffix = ''.join(random.choices(string.digits, k=3))
                await channel.send(f"<@{t_id}> {msg} | `{suffix}`")
                await asyncio.sleep(0.3) 
            except discord.errors.HTTPException as e:
                if e.status == 429: await asyncio.sleep(e.retry_after)
                else: await asyncio.sleep(2)
            except: await asyncio.sleep(2)
    else:
        print("KHÔNG TÌM THẤY KÊNH! Kiểm tra lại CHANNEL_ID")

@client.event
async def on_ready():
    print(f"ACC CHÍNH ĐÃ ONLINE: {client.user}")
    client.loop.create_task(start_raid())

if __name__ == "__main__":
    Thread(target=run).start()
    # Chạy bằng Token acc chính (Không có Bot prefix)
    token = os.getenv('DISCORD_TOKEN')
    try:
        client.run(token, bot=False) # Quan trọng: bot=False
    except Exception as e:
        print(f"Lỗi: {e}")
