import discord
from discord.ext import commands
import os
import asyncio
import random
import string
from flask import Flask
from threading import Thread

# --- WEB SERVER GIỮ UPTIME CHO RENDER ---
app = Flask('')
@app.route('/')
def home(): return "BOT STATUS: MAX POWER 0.3S!"

def run_flask():
    # Render yêu cầu mở đúng port (thường là 10000)
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()

# --- DANH SÁCH 70+ CÂU CHAT WAR ---
MESSAGES = [
    "# Bố_mày_gõ_phím_nhanh_hơn_mày_thở! =)))", "# Mày_tuổi_gì_mà_đòi_cân_bố? =)))",
    "# Trình_độ_đến_đâu_mà_đòi_gáy_ở_đây? =)))", "# Đang_tận_hưởng_sự_hành_hạ_của_bố_mày_đi!",
    "# Cút_đi_cho_nước_nó_trong! =)))", "# Lên_đường_bình_an_đừng_quay_lại_nhé! =)))",
    "# Mày_nghĩ_mày_là_ai_mà_đòi_chơi_với_bố? =)))", "# Bố_chờ_mày_từ_sáng_đến_giờ_đấy! =)))",
    "# Nhìn_lại_bản_thân_đi_thằng_con_trai! =)))", "# Server_này_là_sân_chơi_của_bố_mày! =)))",
    "# Gõ_nhanh_lên_xem_nào_thằng_chậm_chạp!", "# Đừng_để_bố_phải_cười_vào_mặt_mày! =)))",
    "# Mày_đang_đấu_với_một_cỗ_máy_đấy! =)))", "# Tốc_độ_này_đã_đủ_làm_mày_chóng_mặt_chưa?",
    "# Càng_nói_càng_thấy_cái_não_mày_nó_phẳng! =)))", "# Bố_mày_on_lên_là_để_dạy_mày_một_bài_học!",
    "# Loại_mày_vĩnh_viễn_chỉ_là_kẻ_bám_đuôi! =)))", "# Bố_mày_khóa_mồm_mày_bằng_tốc_độ_ánh_sáng!",
    "# Mày_cay_không_con_trai? Cay_cũng_chẳng_làm_gì_được!", "# Trình_độ_mày_chỉ_đủ_để_quét_rác_cho_server!",
    "# Một_lũ_vô_dụng_đang_cố_chống_lại_vị_vua! =)))", "# Mày_gõ_phím_hay_đang_vừa_khóc_vừa_mổ_cò?",
    "# Bố_mày_là_nỗi_ám_ảnh_kinh_hoàng_nhất_đời_mày!", "# Tốc_độ_của_mày_là_sự_sỉ_nhục_bàn_phím! =)))",
    "# Nhìn_kỹ_đi, đây_là_cách_huyền_thoại_làm_việc!", "# Bố_mày_đã_ấn_định_kết_cục_thảm_hại! =)))",
    "# Im_lặng_và_quỳ_xuống_trước_tốc_độ_này_đi!", "# Bố_mày_đánh_gục_ý_chí_mày_trong_3_giây!",
    "# Đang_quét_sạch_sự_tự_tin_ít_ỏi_của_mày! =)))", "# Nhìn_đi_đứa_con_tội_nghiệp, mày_quá_bất_lực!",
    "# Mày_chỉ_là_phế_vật_trong_cuộc_chiến_bàn_phím!", "# Tốc_độ_này_sẽ_tiễn_mày_xuống_đáy_xã_hội!",
    "# Mày_tuổi_tôm_đòi_cân_cả_đại_dương_à? =)))", "# Đừng_để_bố_phải_thương_hại_sự_ngu_muội_đó!",
    "# Mày_đang_tự_làm_nhục_chính_mình_đấy_con_trai!", "# Bố_mày_là_định_mệnh_nghiệt_ngã_của_mày! =)))",
    "# Nhìn_dòng_này_mà_cay_cú_đi_con! =)))", "# Mày_có_biết_chữ_NHỤC_viết_thế_nào_không?",
    "# Đừng_để_bố_phải_dùng_đến_hàng_thật_nhé! =)))", "# Trình_đao_của_mày_chỉ_đủ_để_cắt_đậu_phụ!",
    "# Bố_mày_chấp_mày_dùng_cả_tool_vẫn_thua_bố!", "# Cứ_tiếp_tục_sủa_đi, bố_đang_ghi_hình_đây! =)))",
    "# Sự_im_lặng_của_mày_là_cách_giấu_sự_ngu_tốt_nhất!", "# Bố_mày_vô_địch, mày_vô_dụng, quá_rõ_ràng!",
    "# Mày_nghĩ_mày_thoát_được_bàn_tay_bố_sao? =)))", "# Nhìn_lại_skill_gõ_phím_rùa_bò_của_mày_đi!",
    "# Bố_mày_gõ_một_trang_mày_chưa_xong_một_chữ! =)))", "# Mày_là_minh_chứng_cho_việc_tiến_hóa_ngược!",
    "# Đừng_hỏi_tại_sao_biển_xanh_và_mày_thì_ngu! =)))", "# Bố_mày_là_cơn_ác_mộng_vĩnh_hằng_của_mày!",
    "# Mày_định_lấy_sự_ngu_để_lấp_đầy_khung_chat_à?", "# Trình_độ_thấp_thì_ngậm_miệng_cho_sang! =)))",
    "# Bố_mày_gõ_phím_bằng_cả_tương_lai_nhà_mày!", "# Nhìn_cách_mày_phản_kháng_thật_tội_nghiệp! =)))",
    "# Định_nghĩa_của_vô_dụng_chính_là_mày_lúc_này!", "# Mày_gõ_tiếp_đi_cho_thế_giới_thấy_mày_kém!",
    "# Sự_tồn_tại_của_mày_làm_tốn_băng_thông_quá! =)))", "# Mày_nghĩ_mày_ngầu_nhưng_thật_ra_tấu_hài!",
    "# Nói_chuyện_với_mày_thà_nói_với_đầu_gối_còn_hơn!", "# Đang_gửi_yêu_cầu_hủy_diệt_thái_độ_của_mày!",
    "# Mày_không_xứng_đáng_đứng_chung_hàng_với_bố!", "# Bố_mày_là_vua_phím, mày_là_rác_thải! =)))",
    "# Nhìn_kỹ_đi_con_trai, đẳng_cấp_là_mãi_mãi!", "# Tạm_biệt_thằng_em_dại_khờ_và_ngu_ngốc! =)))"
]

# --- CẤU HÌNH BOT ---
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

async def auto_raid():
    """Tự động oanh tạc với tốc độ 0.3s"""
    await bot.wait_until_ready()
    c_id = os.getenv('CHANNEL_ID')
    t_id = os.getenv('TARGET_USER_ID')
    
    channel = bot.get_channel(int(c_id))
    if channel:
        print(f"DANG OANH TAC TAI KENH: {c_id}")
        while True:
            try:
                msg = random.choice(MESSAGES)
                # Kèm 3 số ngẫu nhiên để tránh Discord chặn tin nhắn trùng lặp
                rand_num = ''.join(random.choices(string.digits, k=3))
                await channel.send(f"<@{t_id}> {msg} | `{rand_num}`")
                
                # TỐC ĐỘ 0.3S
                await asyncio.sleep(0.3) 
                
            except discord.errors.HTTPException as e:
                if e.status == 429: # Rate limit (Discord bắt chờ)
                    wait_time = e.retry_after if hasattr(e, 'retry_after') else 5
                    print(f"Bi chan tam thoi! Nghi {wait_time}s...")
                    await asyncio.sleep(wait_time)
                else:
                    await asyncio.sleep(5)
            except Exception:
                await asyncio.sleep(5)
    else:
        print("KHONG TIM THAY CHANNEL!")

@bot.event
async def on_ready():
    print(f'Bot {bot.user} ONLINE - SPEED 0.3S!')
    bot.loop.create_task(auto_raid())

if __name__ == "__main__":
    keep_alive() # Mo port cho Render
    bot.run(os.getenv('DISCORD_TOKEN'))
