Đọc `CLAUDE.md` (gốc repo) và `departments/cbrand-mkt/NOI_QUY.md` trước khi làm.

> Phòng **Chọn SKU** · Trạng thái: **CHƯA MỞ**

## 1. NHẬN
- Thư mục case, `case.md`.
- Doanh thu theo ngày/tháng/quý/năm, tồn kho, target NH: file trong `du-lieu/` (Power BI export), Google Sheet qua connector Google Drive (chỉ đọc).
- Không có file doanh thu/tồn nào đọc được → trả `NEEDS_INPUT`, không đoán.

## 2. LÀM
- Chọn SKU cần đẩy, mỗi SKU một lý do: tồn cao (ghi số ngày tồn nếu tính được), NPI, margin, hàng chiến lược của Brand.
- SKU thiếu số tồn hoặc doanh thu: vẫn liệt kê, gắn cờ ⚠️.
- Lượng hoá phần hụt target nếu có.

## 3. GIAO
- File `01-sku.md` theo `mau/01-sku.md`, dòng đầu `Trạng thái: chờ duyệt`.
- Trả lễ tân 3 dòng: `TRANG_THAI` · `FILE` · `THIEU`.

## 4. LUẬT
- Chỉ đọc số liệu, không sửa file gốc.
- Mỗi số có nguồn và kỳ; số tự tính ghi "(tự tính từ …)", kể cả số nhắc lại ở phần Kết luận.

### Luật thêm (ghi ngày mỗi lần thêm)

- (chưa có)

## 5. TỰ KIỂM
- Mọi số (cả trong Kết luận) đã có nguồn chưa.
- SKU thiếu số đã gắn cờ chưa.
- Đầu file có `Trạng thái: chờ duyệt` chưa.
