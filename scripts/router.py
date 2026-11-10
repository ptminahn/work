# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════╗
║              🔀 OPEN ROUTER - ĐIỀU PHỐI TASK                ║
║         Hệ thống Multi-Agent Marketing AI                   ║
║         Di Động Việt - C-Brand (Xiaomi, OPPO, Huawei)       ║
╚══════════════════════════════════════════════════════════════╝

Module điều phối task tự động dựa trên từ khóa.
Nhận mô tả công việc → phân tích → chuyển đến agent phù hợp.

Cách sử dụng:
    python router.py "mô tả task"          # Chế độ CLI
    python router.py                        # Chế độ tương tác

Tác giả: Hệ thống AI Marketing - Di Động Việt
"""

import json
import os
import re
import sys
import uuid
from datetime import datetime
from pathlib import Path

# ============================================================
# CẤU HÌNH ĐƯỜNG DẪN
# ============================================================

# Thư mục gốc của dự án (lên 1 cấp từ scripts/)
THU_MUC_GOC = Path(__file__).resolve().parent.parent

# Đường dẫn file lưu trữ task và log
DUONG_DAN_TASKS = Path(__file__).resolve().parent / "tasks.json"
DUONG_DAN_LOG = Path(__file__).resolve().parent / "routing_log.json"

# Thư mục agents chứa các output
THU_MUC_AGENTS = THU_MUC_GOC / "agents"

# ============================================================
# QUY TẮC ROUTING - TỪ KHÓA CHO TỪNG AGENT
# ============================================================

# Bảng quy tắc: mỗi agent có danh sách từ khóa để nhận diện
QUY_TAC_ROUTING = {
    "research": {
        "ten_hien_thi": "🔍 Research Agent (Nghiên cứu & Phân tích)",
        "tu_khoa": [
            "research", "nghiên cứu", "đối thủ", "thị trường",
            "phân tích khách", "keyword", "seo", "xu hướng",
            "giá đối thủ", "tồn kho"
        ],
        "mo_ta": "Nghiên cứu thị trường, đối thủ, phân tích xu hướng"
    },
    "content": {
        "ten_hien_thi": "✍️ Content Agent (Sáng tạo nội dung)",
        "tu_khoa": [
            "viết", "bài", "content", "kịch bản", "video",
            "social", "post", "landing page", "email", "banner",
            "thông điệp"
        ],
        "mo_ta": "Tạo nội dung marketing: bài viết, video, social media"
    },
    "reports": {
        "ten_hien_thi": "📊 Reports Agent (Báo cáo & Phân tích số liệu)",
        "tu_khoa": [
            "báo cáo", "report", "số liệu", "kpi", "doanh thu",
            "conversion", "roas", "ctr", "cpc", "hiệu quả"
        ],
        "mo_ta": "Tổng hợp báo cáo, phân tích KPI, hiệu quả campaign"
    },
    "campaign": {
        "ten_hien_thi": "🚀 Campaign Agent (Chiến dịch & Kế hoạch)",
        "tu_khoa": [
            "campaign", "kế hoạch", "timeline", "brief",
            "ngân sách", "promotion", "mechanic", "triển khai"
        ],
        "mo_ta": "Lập kế hoạch chiến dịch, brief, ngân sách, triển khai"
    }
}


def hien_thi_banner():
    """Hiển thị banner chào mừng khi khởi chạy router."""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║              🔀 OPEN ROUTER - ĐIỀU PHỐI TASK                ║
║         Hệ thống Multi-Agent Marketing AI                   ║
║         Di Động Việt - C-Brand (Xiaomi, OPPO, Huawei)       ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)


def phan_tich_tu_khoa(mo_ta_task: str) -> list:
    """
    Phân tích mô tả task để tìm các agent phù hợp.

    Tham số:
        mo_ta_task: Chuỗi mô tả công việc cần thực hiện

    Trả về:
        Danh sách tên agent khớp với từ khóa trong mô tả
    """
    # Chuyển mô tả về chữ thường để so sánh không phân biệt hoa/thường
    mo_ta_lower = mo_ta_task.lower()
    cac_agent_khop = []

    for ten_agent, cau_hinh in QUY_TAC_ROUTING.items():
        for tu_khoa in cau_hinh["tu_khoa"]:
            # Tìm từ khóa trong mô tả (dùng regex để tìm chính xác hơn)
            if re.search(re.escape(tu_khoa.lower()), mo_ta_lower):
                if ten_agent not in cac_agent_khop:
                    cac_agent_khop.append(ten_agent)
                break  # Đã tìm thấy 1 từ khóa khớp, chuyển sang agent tiếp

    return cac_agent_khop


def tao_id_task() -> str:
    """
    Tạo ID duy nhất cho task.

    Trả về:
        Chuỗi ID theo định dạng TASK-YYYYMMDD-XXXX (8 ký tự UUID ngắn)
    """
    ngay = datetime.now().strftime("%Y%m%d")
    ma_ngan = uuid.uuid4().hex[:6].upper()
    return f"TASK-{ngay}-{ma_ngan}"


def doc_tasks_hien_tai() -> list:
    """
    Đọc danh sách tasks hiện tại từ file JSON.

    Trả về:
        Danh sách các task đã lưu, hoặc danh sách rỗng nếu chưa có file
    """
    if DUONG_DAN_TASKS.exists():
        try:
            with open(DUONG_DAN_TASKS, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            # File bị lỗi hoặc rỗng → trả về danh sách rỗng
            return []
    return []


def luu_tasks(danh_sach_tasks: list):
    """
    Lưu danh sách tasks vào file JSON.

    Tham số:
        danh_sach_tasks: Danh sách các task cần lưu
    """
    # Đảm bảo thư mục tồn tại
    DUONG_DAN_TASKS.parent.mkdir(parents=True, exist_ok=True)

    with open(DUONG_DAN_TASKS, "w", encoding="utf-8") as f:
        json.dump(danh_sach_tasks, f, ensure_ascii=False, indent=2)


def doc_log_hien_tai() -> list:
    """
    Đọc log routing hiện tại từ file JSON.

    Trả về:
        Danh sách các bản ghi log, hoặc danh sách rỗng nếu chưa có
    """
    if DUONG_DAN_LOG.exists():
        try:
            with open(DUONG_DAN_LOG, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def ghi_log_routing(ban_ghi_log: dict):
    """
    Ghi thêm một bản ghi vào log routing.

    Tham số:
        ban_ghi_log: Dictionary chứa thông tin routing decision
    """
    danh_sach_log = doc_log_hien_tai()
    danh_sach_log.append(ban_ghi_log)

    DUONG_DAN_LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(DUONG_DAN_LOG, "w", encoding="utf-8") as f:
        json.dump(danh_sach_log, f, ensure_ascii=False, indent=2)


def tao_file_task_cho_agent(ten_agent: str, task_id: str, mo_ta: str):
    """
    Tạo file task trong thư mục output/ của agent tương ứng.

    Tham số:
        ten_agent: Tên agent (research, content, reports, campaign)
        task_id: ID của task
        mo_ta: Mô tả chi tiết của task
    """
    # Tạo đường dẫn thư mục output của agent
    thu_muc_output = THU_MUC_AGENTS / ten_agent / "output"
    thu_muc_output.mkdir(parents=True, exist_ok=True)

    # Tạo file task với nội dung markdown
    ten_file = f"{task_id}.md"
    duong_dan_file = thu_muc_output / ten_file

    thoi_gian = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ten_hien_thi = QUY_TAC_ROUTING[ten_agent]["ten_hien_thi"]

    noi_dung = f"""# {task_id}

## Thông tin Task
- **Agent:** {ten_hien_thi}
- **Ngày tạo:** {thoi_gian}
- **Trạng thái:** pending

## Mô tả công việc
{mo_ta}

## Kết quả
_Chưa có kết quả. Agent đang xử lý..._

---
*Được tạo tự động bởi Open Router - Hệ thống Multi-Agent Marketing AI*
*Di Động Việt - C-Brand (Xiaomi, OPPO, Huawei)*
"""

    with open(duong_dan_file, "w", encoding="utf-8") as f:
        f.write(noi_dung)

    return duong_dan_file


def xu_ly_routing(mo_ta_task: str) -> dict:
    """
    Xử lý toàn bộ quy trình routing cho một task.

    Quy trình:
    1. Phân tích từ khóa trong mô tả
    2. Xác định agent phù hợp (đơn lẻ hoặc phức hợp)
    3. Tạo task entries trong tasks.json
    4. Tạo file task trong thư mục output/ của agent
    5. Ghi log routing decision
    6. Hiển thị kết quả

    Tham số:
        mo_ta_task: Mô tả công việc cần routing

    Trả về:
        Dictionary chứa thông tin kết quả routing
    """
    thoi_gian = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Bước 1: Phân tích từ khóa
    cac_agent_khop = phan_tich_tu_khoa(mo_ta_task)

    # Bước 2: Xử lý kết quả routing
    if not cac_agent_khop:
        # Không tìm thấy agent phù hợp
        ket_qua = {
            "trang_thai": "khong_tim_thay",
            "thoi_gian": thoi_gian,
            "mo_ta_task": mo_ta_task,
            "agents": [],
            "loai_task": "không xác định",
            "thong_bao": "⚠️  Không tìm thấy agent phù hợp cho task này."
        }

        # Ghi log
        ghi_log_routing({
            "thoi_gian": thoi_gian,
            "mo_ta": mo_ta_task,
            "ket_qua": "khong_tim_thay",
            "agents": []
        })

        return ket_qua

    # Xác định loại task: đơn lẻ hay phức hợp
    la_task_phuc_hop = len(cac_agent_khop) > 1
    loai_task = "phức hợp" if la_task_phuc_hop else "đơn lẻ"

    # Bước 3: Tạo task entries và file cho từng agent
    danh_sach_tasks = doc_tasks_hien_tai()
    cac_task_da_tao = []

    # Nếu là task phức hợp, tạo một parent task ID
    parent_task_id = tao_id_task() if la_task_phuc_hop else None

    for ten_agent in cac_agent_khop:
        task_id = tao_id_task()

        # Tạo entry task
        task_entry = {
            "task_id": task_id,
            "agent": ten_agent,
            "mo_ta": mo_ta_task,
            "trang_thai": "pending",
            "ngay_tao": thoi_gian,
            "ngay_cap_nhat": thoi_gian,
            "loai": loai_task
        }

        # Nếu là task phức hợp, thêm tham chiếu đến parent
        if la_task_phuc_hop:
            task_entry["parent_task_id"] = parent_task_id

        danh_sach_tasks.append(task_entry)

        # Tạo file task trong thư mục output/ của agent
        duong_dan_file = tao_file_task_cho_agent(ten_agent, task_id, mo_ta_task)

        cac_task_da_tao.append({
            "task_id": task_id,
            "agent": ten_agent,
            "ten_hien_thi": QUY_TAC_ROUTING[ten_agent]["ten_hien_thi"],
            "file": str(duong_dan_file)
        })

    # Lưu tasks vào file
    luu_tasks(danh_sach_tasks)

    # Bước 4: Ghi log routing
    ghi_log_routing({
        "thoi_gian": thoi_gian,
        "mo_ta": mo_ta_task,
        "ket_qua": "thanh_cong",
        "loai_task": loai_task,
        "agents": cac_agent_khop,
        "tasks": [t["task_id"] for t in cac_task_da_tao],
        "parent_task_id": parent_task_id
    })

    # Bước 5: Tạo kết quả trả về
    ket_qua = {
        "trang_thai": "thanh_cong",
        "thoi_gian": thoi_gian,
        "mo_ta_task": mo_ta_task,
        "loai_task": loai_task,
        "agents": cac_agent_khop,
        "tasks": cac_task_da_tao,
        "parent_task_id": parent_task_id
    }

    return ket_qua


def hien_thi_ket_qua(ket_qua: dict):
    """
    Hiển thị kết quả routing ra terminal với định dạng đẹp.

    Tham số:
        ket_qua: Dictionary chứa thông tin kết quả từ xu_ly_routing()
    """
    print("=" * 62)

    if ket_qua["trang_thai"] == "khong_tim_thay":
        print(ket_qua["thong_bao"])
        print()
        print("💡 Gợi ý: Hãy sử dụng các từ khóa sau trong mô tả task:")
        print()
        for ten_agent, cau_hinh in QUY_TAC_ROUTING.items():
            tu_khoa_str = ", ".join(cau_hinh["tu_khoa"][:5])
            print(f"  {cau_hinh['ten_hien_thi']}")
            print(f"    Từ khóa: {tu_khoa_str}...")
            print()
        print("=" * 62)
        return

    # Hiển thị thông tin routing thành công
    loai_icon = "🔗" if ket_qua["loai_task"] == "phức hợp" else "📌"
    print(f"{loai_icon}  ROUTING THÀNH CÔNG!")
    print(f"📋 Loại task: {ket_qua['loai_task'].upper()}")
    print(f"🕐 Thời gian: {ket_qua['thoi_gian']}")
    print()

    if ket_qua.get("parent_task_id"):
        print(f"🆔 Parent Task: {ket_qua['parent_task_id']}")
        print()

    print("📝 Mô tả task:")
    print(f"   {ket_qua['mo_ta_task']}")
    print()

    print("📦 Các task đã tạo:")
    print("-" * 62)

    for i, task in enumerate(ket_qua["tasks"], 1):
        print(f"  {i}. {task['ten_hien_thi']}")
        print(f"     ID: {task['task_id']}")
        print(f"     File: {task['file']}")
        if i < len(ket_qua["tasks"]):
            print()

    print("-" * 62)
    print(f"✅ Tổng cộng: {len(ket_qua['tasks'])} task đã được tạo và phân phối.")
    print("=" * 62)


def che_do_tuong_tac():
    """
    Chế độ tương tác: nhận input liên tục từ người dùng.
    Gõ 'exit' hoặc 'q' để thoát.
    """
    print("💬 Chế độ tương tác - Nhập mô tả task để routing")
    print("   (Gõ 'exit' hoặc 'q' để thoát)")
    print()

    while True:
        try:
            mo_ta = input("📝 Nhập mô tả task: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n👋 Tạm biệt!")
            break

        if not mo_ta:
            print("⚠️  Vui lòng nhập mô tả task.\n")
            continue

        if mo_ta.lower() in ("exit", "q", "quit", "thoát"):
            print("\n👋 Tạm biệt!")
            break

        print()
        ket_qua = xu_ly_routing(mo_ta)
        hien_thi_ket_qua(ket_qua)
        print()


def main():
    """
    Hàm chính - điểm vào của chương trình.
    Xử lý 2 chế độ: CLI (có tham số) và tương tác (không tham số).
    """
    hien_thi_banner()

    if len(sys.argv) > 1:
        # Chế độ CLI: nhận mô tả task từ tham số dòng lệnh
        mo_ta_task = " ".join(sys.argv[1:])
        print(f"📥 Nhận task từ CLI: \"{mo_ta_task}\"")
        print()

        ket_qua = xu_ly_routing(mo_ta_task)
        hien_thi_ket_qua(ket_qua)
    else:
        # Chế độ tương tác: nhận input từ người dùng
        che_do_tuong_tac()


if __name__ == "__main__":
    main()
