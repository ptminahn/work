# Cấu hình phòng C-Brand

> Minahn điền và cập nhật file này. Agent chỉ đọc, không tự sửa.

## Ngưỡng GATE 2

- Ngưỡng ngân sách ước lượng cho mỗi case: **[cần Minahn điền, ví dụ: 50.000.000đ]**
- Khi ô trên chưa điền, mọi case có ngân sách ước lượng đều phải dừng ở GATE 2 và ghi "chưa có ngưỡng GATE 2".

## Nguồn dữ liệu

| Nguồn | Chỗ lấy | Cách agent đọc |
|---|---|---|
| Doanh thu, tồn kho (Power BI) | [link dashboard] | Chưa có connector Power BI → Minahn export CSV/XLSX vào `du-lieu/` |
| Google Sheet doanh thu / tồn | [link sheet] | Qua connector Google Drive (chỉ đọc) |
| Report Hero Digital Ads | [link] | File trong `du-lieu/` hoặc Google Drive |
| Báo cáo Ngành hàng | [link] | File trong `du-lieu/` hoặc Google Drive |
| Lịch campaign tổng của BC | [link] | File trong `du-lieu/` hoặc Google Drive |
| Lark Tasks | — | Chưa nối. `task-digest` chưa chạy được |

## Đối thủ theo dõi

CellphoneS, Thế Giới Di Động, FPT Shop, Hoàng Hà Mobile. Bổ sung nếu cần: […]

## Lịch

- Report tuần: [thứ, giờ]
- Task digest: 9h10, Thứ Hai đến Thứ Sáu (chưa chạy được vì chưa nối Lark)
