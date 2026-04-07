import discord
import os, asyncio, random, string
from flask import Flask
from threading import Thread

# --- WEB SERVER GIỮ UPTIME ---
app = Flask('')
@app.route('/')
def home(): return "ACC CHINH DANG CHAY..."

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

async def raid_task():
    await client.wait_until_ready()
    # Ép kiểu ID về số nguyên (int)
    c_id = int(os.getenv('CHANNEL_ID'))
    t_id = os.getenv('TARGET_USER_ID')
    
    channel = client.get_channel(c_id)
    if channel:
        print(f"DA TIM THAY KENH {c_id} - BAT DAU VA 0.3S")
        while True:
            try:
                msg = random.choice(MESSAGES)
                # Dùng mã ngẫu nhiên 4 số để lách bộ lọc spam của Discord
                suffix = ''.join(random.choices(string.digits, k=4))
                await channel.send(f"<@{t_id}> {msg} | `{suffix}`")
                
                # Tốc độ 0.3s
                await asyncio.sleep(0.3)
                
            except discord.errors.HTTPException as e:
                if e.status == 429: # Bị Discord chặn tạm thời
                    print(f"Bị Rate Limit, nghỉ {e.retry_after}s...")
                    await asyncio.sleep(e.retry_after)
                else:
                    await asyncio.sleep(2)
            except Exception as e:
                print(f"Loi: {e}")
                await asyncio.sleep(2)
    else:
        print("KHONG TIM THAY KENH! Check lai CHANNEL_ID ngay!")

@client.event
async def on_ready():
    print(f"DA DANG NHAP ACC CHINH: {client.user}")
    # Đảm bảo task này chạy ngay khi online
    client.loop.create_task(raid_task())

if __name__ == "__main__":
    Thread(target=run).start()
    token = os.getenv('DISCORD_TOKEN')
    # BẮT BUỘC: bot=False để Discord nhận diện là tài khoản người dùng
    client.run(token, bot=False)
