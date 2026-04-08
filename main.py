import discord
import os, asyncio, random
from flask import Flask
from threading import Thread

# Web Server giữ uptime
app = Flask('')
@app.route('/')
def home(): return "BOT IS RUNNING"

def run_web():
    app.run(host='0.0.0.0', port=10000)

MESSAGES = [
    "Mày là cái loại thất học, mở mồm ra là thấy sự ngu dốt!",
    "Trình độ văn hóa thấp kém thì đừng có ra đây gáy với bố!",
    "Mày là bằng chứng sống của việc học chưa hết lớp 1!",
    "Cái loại vô học như mày chỉ đáng làm rác thải xã hội thôi!",
    "Mày gõ phím mà chữ nghĩa lộn xộn như cái đầu thất học của mày!",
    "Mày bị đuổi học từ mẫu giáo đúng không con trai? Nhìn ngu quá!",
    "Loại thất học như mày thì biết cái gì là tư cách?",
    "Học thức không có thì tốt nhất là ngậm mồm vào cho sang!",
    "Nhìn cách mày gõ chữ là biết cả đời chưa đụng vào quyển sách!",
    "Mày là sự sỉ nhục của ngành giáo dục nước nhà!",
    "Mày gáy nữa đi thằng vô học? Sao im thin thít thế?",
    "Bố mày dạy cho mày một bài học về lễ độ này thằng thất học!",
    "Mày là cái loại rác rưởi nhất mà bố từng gặp, thằng thất học!",
    "Gáy nữa đi con, tiếng gáy của thằng vô học nghe vui tai lắm!",
    "Tiễn thằng thất học như mày về nơi an nghỉ cho sạch Discord!"
]

client = discord.Client()

async def raid_engine():
    await client.wait_until_ready()
    print(f"--- ONLINE: {client.user} ---")
    
    # Lấy ID kênh và ID mục tiêu
    channel_id = int(os.environ.get('CHANNEL_ID'))
    target_id = os.environ.get('TARGET_USER_ID')
    channel = await client.fetch_channel(channel_id)
    
    while True:
        try:
            msg = random.choice(MESSAGES)
            # Ký tự tàng hình lách luật spam
            hidden = "\u200b" * random.randint(1, 10)
            
            # Gửi tin nhắn: # Chữ To + Tag
            await channel.send(f"# {msg} \n<@{target_id}>{hidden}")
            print(f"Da va: {msg[:15]}")
        except Exception as e:
            print(f"Loi: {e}")
        
        # Tốc độ 2.5 giây
        await asyncio.sleep(2.5)

@client.event
async def on_ready():
    client.loop.create_task(raid_engine())

if __name__ == "__main__":
    Thread(target=run_web).start()
    # Lấy token trực tiếp
    token = os.environ.get('DISCORD_TOKEN')
    client.run(token, bot=False)
