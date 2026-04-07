import discord
import os, asyncio, random, string
from flask import Flask
from threading import Thread

# --- WEB SERVER GIỮ UPTIME ---
app = Flask('')
@app.route('/')
def home(): return "STATUS: RAIDING - 2.5S DELAY"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- DANH SÁCH 50+ CÂU NGÔN THẤT HỌC ---
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
    "Cái đầu mày chỉ để trang trí chứ kiến thức có chữ nào đâu?",
    "Mày là đứa con rơi của sự ngu dốt và thất học!",
    "Đúng là cái loại không được dạy dỗ tử tế, hèn hạ vô cùng!",
    "Mày gáy nữa đi con, tiếng gáy của thằng vô học nghe vui tai lắm!",
    "Mày là đồ bỏ đi, từ nhân cách đến học thức đều bằng không!",
    "Bố mày ban cho mày cái chết êm ái bằng tốc độ!",
    "Mày gõ phím mà như đang sủa ấy, đúng là cái đồ vô học!",
    "Nhìn mày bố thấy tương lai của sự ngu dốt đang tỏa sáng!",
    "Mày là kẻ thất bại toàn tập vì cái đầu rỗng tuếch thất học!",
    "Tiễn thằng thất học như mày về nơi an nghỉ cho sạch Discord!"
]

client = discord.Client()

async def raid_engine():
    await client.wait_until_ready()
    print(f"--- DA ONLINE ACC: {client.user} ---")
    
    try:
        c_id = int(os.getenv('CHANNEL_ID').strip())
        t_id = os.getenv('TARGET_USER_ID').strip()
        channel = await client.fetch_channel(c_id)
        
        while True:
            try:
                msg = random.choice(MESSAGES)
                # Ký tự trắng tàng hình ngẫu nhiên (Zero Width Space)
                hidden_suffix = "\u200b" * random.randint(1, 20)
                
                # Cấu trúc: # Chữ To + Xuống dòng + Tag cuối + Ký tự tàng hình
                content = f"# {msg} \n<@{t_id}>{hidden_suffix}"
                
                await channel.send(content)
                print(f"-> Đã vả (2.5s): {msg[:20]}...")
            except discord.errors.HTTPException as e:
                if e.status == 429: # Nếu dính Rate Limit
                    print("!!! DÍNH RATE LIMIT - ĐANG NGHỈ 15S !!!")
                    await asyncio.sleep(15)
                else:
                    print(f"Lỗi gửi: {e}")
            except Exception as e:
                print(f"Lỗi: {e}")
                await asyncio.sleep(2)
            
            # ĐỔI THÀNH 2.5 GIÂY (Cộng thêm tí random để né quét)
            delay = 2.5 + random.uniform(0.1, 0.3)
            await asyncio.sleep(delay)
            
    except Exception as e:
        print(f"Lỗi khởi động: {e}")

@client.event
async def on_ready():
    client.loop.create_task(raid_engine())

if __name__ == "__main__":
    Thread(target=run_web).start()
    token = os.getenv('DISCORD_TOKEN').strip()
    try:
        client.run(token, bot=False)
    except:
        client.run(token)
