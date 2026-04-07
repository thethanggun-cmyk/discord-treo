import discord
import os
import asyncio
import random
import string
from flask import Flask
from threading import Thread

# --- WEB SERVER GIỮ UPTIME ---
app = Flask('')
@app.route('/')
def home(): return "ACC CHINH DANG WAR..."

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
    "Bố mày là nỗi ám ảnh kinh hoàng nhất đời mày!", "Tốc độ của mày là sự sỉ nhục bàn phím! =)))",
    "Im lặng và quỳ xuống trước tốc độ này đi!", "Bố mày đánh gục ý chí mày trong 3 giây!",
    "Mày chỉ là phế vật trong cuộc chiến bàn phím!", "Tốc độ này sẽ tiễn mày xuống đáy xã hội!",
    "Mày tuổi tôm đòi cân cả đại dương à? =)))", "Bố mày chấp mày dùng cả tool vẫn thua bố!",
    "Bố mày vô địch, mày vô dụng, quá rõ ràng!", "Mày là minh chứng cho việc tiến hóa ngược!",
    "Trình độ thấp thì ngậm miệng cho sang! =)))", "Mày gõ tiếp đi cho thế giới thấy mày kém!",
    "Bố mày là vua phím, mày là rác thải! =)))"
]

# --- CẤU HÌNH ACC CHÍNH ---
client = discord.Client()

async def raid_task():
    await client.wait_until_ready()
    c_id = os.getenv('CHANNEL_ID')
    t_id = os.getenv('TARGET_USER_ID')
    
    channel = client.get_channel(int(c_id))
    if channel:
        print(f"ĐÃ VÀO KÊNH {c_id} - CHUẨN BỊ VẢ 0.3S")
        while True:
            try:
                msg = random.choice(MESSAGES)
                # Acc chính BẮT BUỘC phải có suffix để lách bộ lọc spam cực gắt của Discord
                suffix = ''.join(random.choices(string.digits, k=4))
                await channel.send(f"<@{t_id}> {msg} | `{suffix}`")
                
                # Tốc độ 0.3s cho acc chính là cực kỳ mạo hiểm, nhưng chiều bạn:
                await asyncio.sleep(0.3)
                
            except discord.errors.Forbidden:
                print("LỖI: Acc không có quyền gửi tin nhắn trong kênh này!")
                break
            except discord.errors.HTTPException as e:
                if e.status == 429: # Bị Rate Limit
                    print(f"Bị chặn tạm thời, chờ {e.retry_after}s...")
                    await asyncio.sleep(e.retry_after)
                else:
                    await asyncio.sleep(2)
            except Exception as e:
                print(f"Lỗi lạ: {e}")
                await asyncio.sleep(2)
    else:
        print("LỖI: Không tìm thấy Kênh chat! Check lại CHANNEL_ID")

@client.event
async def on_ready():
    print(f"ACC CHÍNH [{client.user}] ĐÃ ONLINE!")
    client.loop.create_task(raid_task())

if __name__ == "__main__":
    Thread(target=run).start()
    token = os.getenv('DISCORD_TOKEN')
    # Quan trọng: bot=False để báo cho thư viện đây là acc người dùng
    client.run(token, bot=False)
