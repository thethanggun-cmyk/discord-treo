import discord
import os, asyncio, random, string
from flask import Flask
from threading import Thread

# --- WEB SERVER ---
app = Flask('')
@app.route('/')
def home(): return "STATUS: CHU TO - SO AN - 50+ CAU"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- 50+ CÂU NGÔN ---
MESSAGES = [
    "Bố mày gõ nhanh hơn mày thở!", "Mày tuổi gì đòi cân bố?",
    "Trình độ đến đâu mà gáy ở đây?", "Cút đi cho nước nó trong!",
    "Bố mày khóa mồm mày bằng tốc độ ánh sáng!", "Mày cay không con trai?",
    "Bố mày là nỗi ám ảnh kinh hoàng!", "Tốc độ của mày là sự sỉ nhục!",
    "Im lặng và quỳ xuống đi!", "Bố mày đánh gục mày trong 3 giây!",
    "Bố mày là vua phím, mày là rác!", "Nhìn lại bản thân đi con trai!",
    "Mày chỉ là hạt cát dưới chân bố!", "Gõ chậm thì về học lại mẫu giáo!",
    "Đừng để bố mày phải ra tay!", "Trình mày chỉ đáng xách dép!",
    "Mày có biến thành tro bố vẫn nhận ra!", "Cay lắm đúng không con trai?",
    "Nhìn mày gõ bố thấy tội nghiệp!", "Tốc độ này không dành cho mày!",
    "Mày gáy nữa đi? Sao im thế?", "Bố mày là tượng đài, mày là rác!",
    "Định dùng tốc độ rùa bò đó đấu với bố?", "Câm mồm nghe bố giảng đạo!",
    "Trình chưa tới đừng có ra gió!", "Mày là sự thất bại của tạo hóa!",
    "Chấp mày gõ trước 10 năm vẫn không kịp!", "Nhìn thẳng vào sự thật đi!",
    "Mày chỉ là giỏi sủa thôi à?", "Bố mày tiễn mày về nơi an nghỉ!",
    "Bố mày cáu là mày mất xác!", "Mày tuổi tôm tuổi tép!",
    "Gõ nhanh lên? Tay run à?", "Mày cay phát khóc rồi đúng không?",
    "Bố mày là cơn ác mộng của mày!", "Trình độ quá kém, thất vọng!",
    "Mày không đủ tư cách đứng trước bố!", "Cút về với mẹ đi con trai!",
    "Bố mày là chân lý, mày là nghịch lý!", "Mày định dùng lưỡi đấu với bố?",
    "Mày chỉ là con rối của bố!", "Bố điều khiển cuộc chơi này!",
    "Mày gáy to nữa lên xem nào?", "Bố dẫm nát sĩ diện của mày!",
    "Mày là kẻ thất bại toàn tập!", "Đừng cố nữa, không thắng được đâu!",
    "Mày chỉ là phế thải xã hội!", "Bố mày xóa sổ mày khỏi Discord!",
    "Nhìn cái mặt mày tội nghiệp chưa?", "Ban cho mày cái chết êm ái!",
    "Mày là đứa con rơi của sự ngu dốt!", "Gõ nữa đi, kịch đang hay!",
    "Tuổi gì chung mâm với bố? Cút!", "Tiễn mày một đoạn đầu thai cho nhanh!"
]

client = discord.Client()

async def raid_engine():
    await client.wait_until_ready()
    print(f"--- ONLINE: {client.user} ---")
    
    try:
        c_id = int(os.getenv('CHANNEL_ID').strip())
        t_id = os.getenv('TARGET_USER_ID').strip()
        channel = await client.fetch_channel(c_id)
        
        while True:
            try:
                msg = random.choice(MESSAGES)
                # Tạo mã ẩn (3 số) nằm trong thẻ spoiler ||
                hidden_code = "".join(random.choices(string.digits, k=3))
                
                # Cấu trúc: # Chữ To + Xuống dòng + Tag Cuối + Mã Ẩn
                full_msg = f"# {msg} \n<@{t_id}> ||{hidden_code}||"
                
                await channel.send(full_msg)
                print(f"-> Đã vả (Mã ẩn: {hidden_code})")
            except Exception as e:
                print(f"Lỗi gửi: {e}")
                await asyncio.sleep(1)
            
            # Tốc độ 0.3s - 0.4s
            await asyncio.sleep(0.35)
            
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
