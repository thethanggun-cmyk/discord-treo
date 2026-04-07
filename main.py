import discord
import os, asyncio, random, string
from flask import Flask
from threading import Thread

# --- WEB SERVER GIỮ UPTIME ---
app = Flask('')
@app.route('/')
def home(): return "STATUS: RAIDING - ZERO WIDTH"

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
    "Mày gõ phím bằng tay hay bằng chân mà chữ nghĩa như rác thế?",
    "Trình độ lớp 1 còn chưa thông mà đòi lên đây đấu với bố à?",
    "Mày là phế phẩm của một nền giáo dục thất bại!",
    "Mày định dùng sự ngu dốt để thắng bố à? Nằm mơ đi con!",
    "Thằng thất học như mày chỉ xứng đáng quỳ dưới chân bố thôi!",
    "Mày có học đến kiếp sau cũng không đuổi kịp trình độ của bố!",
    "Mày là cái loại cặn bã, vừa ngu vừa lì lại còn thất học!",
    "Mở não ra mà học hỏi đi thằng vô học, nhìn mày tội nghiệp quá!",
    "Mày không có não hay là não mày bị thất học nó ăn mất rồi?",
    "Mày là vết nhơ của dòng họ vì cái sự thất học của mày đó!",
    "Cút về học lại cách làm người trước khi ra đây gáy với bố!",
    "Mày định lấy cái bằng thất học ra để khè bố à? Nực cười!",
    "Sự ngu dốt của mày là vô tận, đúng chất một thằng vô học!",
    "Mày gáy to lên cho cả thế giới biết mày thất học đi con!",
    "Bố mày khinh cái loại không có học thức như mày!",
    "Mày gõ chữ mà bố thấy xấu hổ thay cho thầy cô giáo của mày!",
    "Loại như mày thì chỉ có đi hốt rác mới xứng tầm kiến thức!",
    "Mày là thiên tài trong lĩnh vực thất học đó con trai!",
    "Mày nhìn lại bản thân đi, có chỗ nào ra dáng người có học không?",
    "Bố mày tát cho mày tỉnh cái đầu thất học ra nhé!",
    "Mày cay lắm đúng không thằng vô học? Cay thì đi học đi!",
    "Mày là nỗi nhục lớn nhất của những người biết chữ!",
    "Mày gõ nhanh lên xem nào? Đầu óc thất học nên tay chân chậm à?",
    "Bố mày xóa sổ cái sự thất học của mày ngay tại đây!",
    "Mày không đủ tư cách để bố mày phải phí lời, thằng vô học!",
    "Mày là kết quả của việc trốn học đi chơi nét quá nhiều đấy!",
    "Mày định dùng sự vô văn hóa để lấp liếm cái ngu của mày à?",
    "Mày là cái loại rác rưởi nhất mà bố từng gặp, thằng thất học!",
    "Gáy nữa đi con, tiếng gáy của thằng vô học nghe vui tai lắm!",
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
                # Tạo chuỗi ký tự trắng tàng hình ngẫu nhiên (Zero Width Space)
                # Discord sẽ thấy tin nhắn khác nhau, nhưng mắt người thấy giống nhau 100%
                hidden_suffix = "\u200b" * random.randint(1, 15)
                
                # Cấu trúc: # Chữ To + Xuống dòng + Tag cuối + Ký tự tàng hình
                content = f"# {msg} \n<@{t_id}>{hidden_suffix}"
                
                await channel.send(content)
                print(f"-> Đã vả (Tàng hình): {msg[:20]}...")
            except Exception as e:
                print(f"Lỗi gửi: {e}")
                await asyncio.sleep(1)
            
            # Tốc độ 0.35s
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
