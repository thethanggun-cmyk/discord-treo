import discord
import os, asyncio, random
from flask import Flask
from threading import Thread

# --- 1. WEB SERVER ĐỂ TREO 24/24 ---
app = Flask('')

@app.route('/')
def home():
    # Link này dùng để dán vào UptimeRobot
    return "BOT STATUS: ALIVE & RAIDING 24/7"

def run_web():
    # Render chạy trên port 10000
    app.run(host='0.0.0.0', port=10000)

# --- 2. DANH SÁCH CÂU CHỬI (NGÔN THẤT HỌC) ---
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
    "Thằng thất học như mày chỉ xứng đáng quỳ dưới chân bố thôi!",
    "Mày định lấy cái bằng thất học ra để khè bố à? Nực cười!",
    "Tiễn thằng thất học như mày về nơi an nghỉ cho sạch Discord!"
]

client = discord.Client()

# --- 3. ENGINE VẢ MỤC TIÊU ---
async def raid_engine():
    print("--- [WAIT] ĐANG CHỜ KẾT NỐI DISCORD... ---")
    await client.wait_until_ready()
    print(f"--- [OK] ĐÃ ĐĂNG NHẬP ACC: {client.user} ---")
    
    # Lấy ID từ tab Environment trên Render
    try:
        c_id = int(os.getenv('CHANNEL_ID').strip())
        t_id = os.getenv('TARGET_USER_ID').strip()
        channel = await client.fetch_channel(c_id)
        
        print(f"--- [TARGET] ĐANG VẢ KÊNH: {channel.name} ---")
        
        while True:
            try:
                msg = random.choice(MESSAGES)
                # Ký tự trắng tàng hình lách luật spam
                hidden = "\u200b" * random.randint(1, 15)
                
                # Định dạng: # (To) + ** (Đậm) + Xuống dòng + Tag
                content = f"# **{msg}** \n<@{t_id}>{hidden}"
                
                await channel.send(content)
                print(f"-> Đã vả: {msg[:20]}...")
            except discord.errors.HTTPException as e:
                if e.status == 429:
                    print("!!! DÍNH RATE LIMIT - NGHỈ 20S !!!")
                    await asyncio.sleep(20)
                else:
                    print(f"Lỗi Discord: {e}")
            except Exception as e:
                print(f"Lỗi gửi tin: {e}")
                await asyncio.sleep(5)
            
            # TỐC ĐỘ 2.5 GIÂY (Có chút random để né quét bot)
            await asyncio.sleep(2.5 + random.uniform(0.1, 0.3))
            
    except Exception as e:
        print(f"--- [LỖI] KHÔNG KHỞI CHẠY ĐƯỢC RAID: {e} ---")

@client.event
async def on_ready():
    client.loop.create_task(raid_engine())

# --- 4. KHỞI CHẠY HỆ THỐNG ---
if __name__ == "__main__":
    print("--- [START] ĐANG NẠP CODE... ---")
    
    # Chạy Web Server giữ uptime ở luồng riêng
    Thread(target=run_web).start()
    
    # Chạy Discord Account
    token = os.getenv('DISCORD_TOKEN')
    if token:
        # Đã xóa 'bot=False' để fix lỗi discord.py-self của mày
        try:
            client.run(token.strip())
        except Exception as e:
            print(f"--- [LỖI] KHÔNG LOGIN ĐƯỢC: {e} ---")
    else:
        print("--- [LỖI] THIẾU DISCORD_TOKEN TRONG TAB ENVIRONMENT! ---")
