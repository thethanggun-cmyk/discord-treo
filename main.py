import discord
import os, asyncio, random, string
from flask import Flask
from threading import Thread

# --- WEB SERVER GIỮ UPTIME ---
app = Flask('')
@app.route('/')
def home(): return "STATUS: DANG VA CHU TO 50+ CAU"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- DANH SÁCH 50+ CÂU NGÔN ---
MESSAGES = [
    "Bố mày gõ nhanh hơn mày thở! =)))", "Mày tuổi gì đòi cân bố? =)))",
    "Trình độ đến đâu mà gáy ở đây? =)))", "Cút đi cho nước nó trong! =)))",
    "Bố mày khóa mồm mày bằng tốc độ ánh sáng!", "Mày cay không con trai? Cay cũng chẳng làm gì được!",
    "Bố mày là nỗi ám ảnh kinh hoàng nhất đời mày!", "Tốc độ của mày là sự sỉ nhục bàn phím! =)))",
    "Im lặng và quỳ xuống trước tốc độ này đi!", "Bố mày đánh gục ý chí mày trong 3 giây!",
    "Bố mày là vua phím, mày là rác thải! =)))", "Nhìn lại bản thân đi thằng con trai! =)))",
    "Mày chỉ là hạt cát dưới chân bố thôi con ạ!", "Gõ chậm thế thì về học lại mẫu giáo đi!",
    "Đừng để bố mày phải ra tay thêm lần nữa!", "Cái trình độ của mày chỉ đáng xách dép cho bố!",
    "Mày có biến thành tro bố vẫn nhận ra cái sự ngu của mày!", "Cay lắm đúng không? Cay thì làm gì được bố? =)))",
    "Nhìn mày gõ mà bố thấy tội nghiệp cho cái bàn phím!", "Tốc độ này là để dành cho những kẻ xứng tầm, không phải mày!",
    "Mày gáy nữa đi? Sao im thin thít thế con trai? =)))", "Bố mày là tượng đài, mày là cỏ rác!",
    "Mày định dùng cái tốc độ rùa bò đó để đấu với bố à?", "Câm mồm vào và nghe bố giảng đạo này!",
    "Trình độ chưa tới thì đừng có ra gió kẻo trúng gió!", "Mày là sự thất bại của tạo hóa con ạ!",
    "Bố mày chấp mày gõ trước 10 năm vẫn không đuổi kịp!", "Nhìn thẳng vào sự thật đi, mày quá yếu kém!",
    "Mày chỉ giỏi sủa thôi chứ làm được gì? =)))", "Bố mày tiễn mày về nơi an nghỉ cuối cùng nhé!",
    "Đừng để bố mày cáu, bố mày cáu là mày mất xác!", "Mày tuổi tôm, tuổi tép, tuổi rác rưởi!",
    "Gõ nhanh lên xem nào? Tay chân run lẩy bẩy thế à?", "Mày cay đến mức phát khóc rồi đúng không? =)))",
    "Bố mày là cơn ác mộng mà mày không bao giờ muốn gặp!", "Trình độ của mày chỉ đến thế thôi sao? Thất vọng quá!",
    "Mày không đủ tư cách để đứng trước mặt bố!", "Cút về với mẹ mày đi con trai, ở đây nguy hiểm lắm!",
    "Bố mày là chân lý, mày là nghịch lý!", "Mày định dùng cái lưỡi không xương để đấu với bố à?",
    "Mày chỉ là con rối trong tay bố thôi!", "Bố mày điều khiển cuộc chơi này, mày chỉ là quân cờ!",
    "Mày gáy to nữa lên? Sao tiếng gáy nhỏ dần thế con?", "Bố mày dẫm nát cái sĩ diện hão của mày!",
    "Mày là kẻ thất bại toàn tập, hiểu chưa con trai? =)))", "Đừng cố gắng nữa, mày không bao giờ thắng được bố!",
    "Mày chỉ là phế thải của xã hội này thôi!", "Bố mày xóa sổ mày khỏi bản đồ Discord này!",
    "Mày nhìn lại cái mặt mày đi, trông có tội nghiệp không?", "Bố mày ban cho mày cái chết êm ái bằng tốc độ!",
    "Mày là đứa con rơi của sự ngu dốt!", "Gõ nữa đi con, bố đang xem kịch hay đây! =)))",
    "Mày tuổi gì mà đòi chung mâm với bố? Cút!", "Bố mày tiễn mày một đoạn cho nhanh đầu thai!"
]

client = discord.Client()

async def raid_engine():
    await client.wait_until_ready()
    print(f"--- DA DANG NHAP: {client.user} ---")
    
    try:
        # Lấy thông tin từ tab Environment của Render
        c_id_raw = os.getenv('CHANNEL_ID', '').strip()
        t_id_raw = os.getenv('TARGET_USER_ID', '').strip()
        
        if not c_id_raw:
            print("!!! THIEU CHANNEL_ID !!!")
            return
            
        channel = await client.fetch_channel(int(c_id_raw))
        print(f"--- DANG CHIEN TAI KENH: {channel.name} ---")
        
        while True:
            try:
                msg = random.choice(MESSAGES)
                # Thêm khoảng trắng tàng hình để né bộ lọc trùng lặp
                invisible_space = " " * random.randint(1, 5)
                
                # Cấu trúc: # Chữ To + Tag Cuối
                content = f"# {msg} {invisible_space} <@{t_id_raw}>"
                
                await channel.send(content)
                print(f"-> Da va: {msg[:20]}...")
            except Exception as e:
                print(f"Loi gui: {e}")
                await asyncio.sleep(2)
            
            # Tốc độ cực nhanh
            await asyncio.sleep(0.3)
            
    except Exception as e:
        print(f"Loi khoi chay: {e}")

@client.event
async def on_ready():
    client.loop.create_task(raid_engine())

if __name__ == "__main__":
    # Chạy Web giữ uptime
    Thread(target=run_web).start()
    
    # Chạy Acc chính
    token = os.getenv('DISCORD_TOKEN', '').strip()
    try:
        client.run(token, bot=False)
    except:
        client.run(token)
