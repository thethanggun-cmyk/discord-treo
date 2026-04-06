import discord
from discord.ext import commands
import os, asyncio, random, string
from flask import Flask
from threading import Thread

# --- PHẦN 1: MỞ CỔNG RENDER CỰC NHANH ---
app = Flask('')
@app.route('/')
def home(): return "BOT ALIVE"

def run():
    # Render bắt buộc phải thấy port này mở
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- PHẦN 2: DANH SÁCH CÂU CHỬI (70+ CÂU) ---
MESSAGES = [
    "Bố mày gõ nhanh hơn mày thở! =)))", "Mày tuổi gì đòi cân bố? =)))",
    "Trình độ đến đâu mà gáy ở đây? =)))", "Cút đi cho nước nó trong! =)))",
    "Nhìn lại bản thân đi thằng con trai! =)))", "Gõ nhanh lên xem nào thằng chậm chạp!",
    "Mày đang đấu với một cỗ máy đấy! =)))", "Tốc độ này đã đủ làm mày chóng mặt chưa?",
    "Càng nói càng thấy cái não mày nó phẳng! =)))", "Bố mày khóa mồm mày bằng tốc độ ánh sáng!",
    "Mày cay không con trai? Cay cũng chẳng làm gì được!", "Trình độ mày chỉ đủ để quét rác cho server!",
    "Một lũ vô dụng đang cố chống lại vị vua! =)))", "Mày gõ phím hay đang vừa khóc vừa mổ cò?",
    "Bố mày là nỗi ám ảnh kinh hoàng nhất đời mày!", "Tốc độ của mày là sự sỉ nhục bàn phím! =)))",
    "Nhìn kỹ đi, đây là cách huyền thoại làm việc!", "Bố mày đã ấn định kết cục thảm hại! =)))",
    "Im lặng và quỳ xuống trước tốc độ này đi!", "Bố mày đánh gục ý chí mày trong 3 giây!",
    "Mày chỉ là phế vật trong cuộc chiến bàn phím!", "Tốc độ này sẽ tiễn mày xuống đáy xã hội!",
    "Mày tuổi tôm đòi cân cả đại dương à? =)))", "Nhìn dòng này mà cay cú đi con! =)))",
    "Đừng để bố phải dùng đến hàng thật nhé! =)))", "Bố mày chấp mày dùng cả tool vẫn thua bố!",
    "Bố mày vô địch, mày vô dụng, quá rõ ràng!", "Nhìn lại skill gõ phím rùa bò của mày đi!",
    "Mày là minh chứng cho việc tiến hóa ngược!", "Bố mày là cơn ác mộng vĩnh hằng của mày!",
    "Trình độ thấp thì ngậm miệng cho sang! =)))", "Bố mày gõ phím bằng cả tương lai nhà mày!",
    "Nhìn cách mày phản kháng thật tội nghiệp! =)))", "Mày gõ tiếp đi cho thế giới thấy mày kém!",
    "Mày nghĩ mày ngầu nhưng thật ra tấu hài!", "Đang gửi yêu cầu hủy diệt thái độ của mày!",
    "Bố mày là vua phím, mày là rác thải! =)))", "Tạm biệt thằng em dại khờ và ngu ngốc! =)))"
]

# --- PHẦN 3: CẤU HÌNH BOT TỐC ĐỘ 0.3S ---
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

async def start_raid():
    await bot.wait_until_ready()
    c_id = os.getenv('CHANNEL_ID')
    t_id = os.getenv('TARGET_USER_ID')
    channel = bot.get_channel(int(c_id))
    
    if channel:
        print(f"BẮT ĐẦU VẢ 0.3S TẠI: {c_id}")
        while True:
            try:
                msg = random.choice(MESSAGES)
                # Kèm 3 số ngẫu nhiên để Discord không báo trùng tin nhắn
                suffix = ''.join(random.choices(string.digits, k=3))
                await channel.send(f"<@{t_id}> {msg} | `{suffix}`")
                await asyncio.sleep(0.3) # TỐC ĐỘ THEO YÊU CẦU CỦA BẠN
            except discord.errors.HTTPException as e:
                if e.status == 429: await asyncio.sleep(e.retry_after)
                else: await asyncio.sleep(1)
            except: await asyncio.sleep(1)

@bot.event
async def on_ready():
    print(f"BOT ONLINE: {bot.user}")
    bot.loop.create_task(start_raid())

if __name__ == "__main__":
    Thread(target=run).start() # Chạy web server ngay lập tức
    bot.run(os.getenv('DISCORD_TOKEN'))
