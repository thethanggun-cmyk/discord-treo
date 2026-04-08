import discord
import os, asyncio, random
from flask import Flask
from threading import Thread

# Web Server giữ uptime
app = Flask('')
@app.route('/')
def home(): return "STATUS: RAIDING - 2.5S"

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
    "Tiễn thằng thất học như mày về nơi an nghỉ cho sạch Discord!"
]

client = discord.Client()

async def raid_engine():
    print("--- [WAIT] DANG CHO KET NOI DISCORD... ---")
    await client.wait_until_ready()
    print(f"--- [OK] DA DANG NHAP: {client.user} ---")
    
    c_id = os.getenv('CHANNEL_ID')
    t_id = os.getenv('TARGET_USER_ID')
    
    try:
        channel = await client.fetch_channel(int(c_id.strip()))
        while True:
            msg = random.choice(MESSAGES)
            hidden = "\u200b" * random.randint(1, 15)
            await channel.send(f"# {msg} \n<@{t_id.strip()}>{hidden}")
            print(f"-> Da va: {msg[:15]}")
            # Speed 2.5s
            await asyncio.sleep(2.5)
    except Exception as e:
        print(f"--- [LOI] KHONG THE GUI TIN: {e} ---")

@client.event
async def on_ready():
    client.loop.create_task(raid_engine())

if __name__ == "__main__":
    print("--- [START] CODE BAT DAU CHAY... ---")
    Thread(target=run_web).start()
    
    token = os.getenv('DISCORD_TOKEN')
    if token:
        # CHỖ NÀY ĐÃ SỬA: Không dùng bot=False nữa
        client.run(token.strip())
    else:
        print("--- [LOI] THIEU TOKEN TRONG ENVIRONMENT ---")
