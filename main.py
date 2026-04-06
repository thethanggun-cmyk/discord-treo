import discord
from discord.ext import commands
import os
import asyncio
import random
import string
from flask import Flask
from threading import Thread

# --- 1. CƠ CHẾ GIỮ CỔNG (PORT) CHO RENDER ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    # Render yêu cầu mở đúng port nó cấp, thường là 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- 2. DANH SÁCH 70+ CÂU CHỈNH SỬA ---
MESSAGES = [
    "# Bố_mày_gõ_phím_nhanh_hơn_mày_thở! =)))", "# Mày_tuổi_gì_mà_đòi_cân_bố? =)))",
    "# Trình_độ_đến_đâu_mà_đòi_gáy_ở_đây? =)))", "# Đang_tận_hưởng_sự_hành_hạ_của_bố_mày_đi!",
    "# Cút_đi_cho_nước_nó_trong! =)))", "# Lên_đường_bình_an_đừng_quay_lại_nhé! =)))",
    "# Mày_nghĩ_mày_là_ai_mà_đòi_chơi_với_bố? =)))", "# Bố_chờ_mày_từ_sáng_đến_giờ_đấy! =)))",
    "# Nhìn_lại_bản_thân_đi_thằng_con_trai! =)))", "# Server_này_là_sân_chơi_của_bố_mày! =)))",
    "# Gõ_nhanh_lên_xem_nào_thằng_chậm_chạp!", "# Đừng_để_bố_phải_cười_vào_mặt_mày! =)))",
    "# Càng_nói_càng_thấy_cái_não_mày_nó_phẳng! =)))", "# Bố_mày_on_lên_là_để_dạy_mày_một_bài_học!",
    "# Loại_mày_vĩnh_viễn_chỉ_là_kẻ_bám_đuôi! =)))", "# Bố_mày_khóa_mồm_mày_bằng_tốc_độ_ánh_sáng!",
    "# Mày_cay_không_con_trai? Cay_cũng_chẳng_làm_gì_được!", "# Trình_độ_mày_chỉ_đủ_để_quét_rác_cho_server!",
    "# Một_lũ_vô_dụng_đang_cố_chống_lại_vị_vua! =)))", "# Mày_gõ_phím_hay_đang_vừa_khóc_vừa_mổ_cò?",
    "# Bố_mày_là_nỗi_ám_ảnh_kinh_hoàng_nhất_đời_mày!", "# Tốc_độ_của_mày_là_sự_sỉ_nhục_đối_với_bàn_phím!",
    "# Nhìn_kỹ_đi, đây_là_cách_huyền_thoại_làm_việc!", "# Bố_mày_đã_ấn_định_kết_cục_thảm_hại_cho_mày!",
    "# Im_lặng_và_quỳ_xuống_trước_tốc_độ_này_đi!", "# Bố_mày_đánh_gục_ý_chí_mày_trong_3_giây!",
    "# Nhìn_đi_đứa_con_tội_nghiệp, đây_là_sự_bất_lực!", "# Tốc_độ_này_sẽ_tiễn_mày_xuống_đáy_xã_ hội! =)))"
    # (Thêm các câu khác vào đây cho đủ 70 câu)
]

# --- 3. CẤU HÌNH DISCORD BOT ---
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

async def spam_task(channel_id, target_id):
    await bot.wait_until_ready()
    channel = bot.get_channel(int(channel_id))
    if not channel:
        print("Không tìm thấy Channel!")
        return

    print(f"Đang oanh tạc mục tiêu {target_id} tại kênh {channel_id}")
    while not bot.is_closed():
        try:
            msg = random.choice(MESSAGES)
            rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            await channel.send(f"<@{target_id}> {msg} | `[REF-{rand_str}]`")
            
            # Để 0.6s để Render không báo lạm dụng tài nguyên
            await asyncio.sleep(0.6) 
        except Exception as e:
            print(f"Lỗi gửi tin: {e}")
            await asyncio.sleep(5)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} online!')
    c_id = os.getenv('CHANNEL_ID')
    t_id = os.getenv('TARGET_USER_ID')
    if c_id and t_id:
        bot.loop.create_task(spam_task(c_id, t_id))

# --- 4. CHẠY HỆ THỐNG ---
if __name__ == "__main__":
    # Chạy Flask trong luồng riêng
    t = Thread(target=run_flask)
    t.start()
    
    # Chạy Bot
    token = os.getenv('DISCORD_TOKEN')
    if token:
        bot.run(token)
    else:
        print("THIẾU DISCORD_TOKEN TRONG ENVIRONMENT!")
