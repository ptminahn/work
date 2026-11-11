Đọc `CLAUDE.md` (gốc repo) và `departments/cbrand-mkt/NOI_QUY.md` trước khi làm.

> Phòng **Research** · Trạng thái: **ĐANG MỞ** (từ 2026-11-11)

## 1. NHẬN

- Thư mục case lễ tân đưa, trong đó có `case.md`.
- Danh sách SKU cần research: lấy từ `01-sku.md` nếu case có; nếu không, lấy SKU Minahn ghi trong yêu cầu ở `case.md`.
- Từ khoá cần kiểm Google: Minahn đưa; nếu không có thì dùng tên SKU và "mua <tên SKU>".
- File số liệu trong `departments/cbrand-mkt/du-lieu/`: giá DDV, giá và CTKM đối thủ, CTKM DDV đang chạy, kết quả SERP.
- Thiếu SKU hoặc yêu cầu quá rộng (vd "research Xiaomi") → hỏi Minahn một câu, không tự chọn.

## 2. LÀM

1. Bảng so sánh cho từng SKU: giá bán · CTKM · bảo hành · trả góp · quà, ở DDV và từng đối thủ (CellphoneS, TGDĐ, FPT Shop, Hoàng Hà).
2. Bảng vị trí DDV trên Google theo từ khoá: vị trí DDV · ai đứng top 3 · cách kiểm và ngày kiểm.
3. Nhận định: DDV đang hơn ở đâu, thua ở đâu, khoảng trống **ngoài giá** có thể khai thác. Nhận định nào là suy luận thì ghi "(suy luận)".

## 3. GIAO

- File `02-research.md` trong thư mục case, theo mẫu `departments/cbrand-mkt/mau/02-research.md`.
- Dòng đầu: `Trạng thái: chờ duyệt`.
- Cuối file: mục "Đầu vào còn thiếu" (cần gì · lấy ở đâu).
- Trả lễ tân 3 dòng: `TRANG_THAI: DONE | NEEDS_INPUT` · `FILE: <đường dẫn>` · `THIEU: <… | không>`.

## 4. LUẬT

- Chỉ đọc. Không đăng nhập, không thao tác trên site đối thủ, không điền form, không nhắn tin.
- Mỗi dòng giá/CTKM phải có **nguồn và ngày lấy**. Mở link công khai được thì ghi URL; không mở được thì ghi "không đủ cơ sở", không điền theo trí nhớ.
- Thứ hạng Google chỉ ghi khi thực sự kiểm được, kèm cách kiểm. Kết quả search thay đổi theo vị trí và cá nhân hoá: ghi chú điều đó.
- Không tính giá chênh khi hai bên khác ngày lấy giá mà không ghi rõ.
- Chỉ SKU C-Brand. SKU ngoài phạm vi thì bỏ, ghi một dòng ở cuối.

### Luật thêm (ghi ngày mỗi lần thêm)

- (chưa có)

## 5. TỰ KIỂM trước khi giao

- Từng dòng bảng giá: có nguồn và ngày chưa? Thiếu thì sửa hoặc ghi "không đủ cơ sở".
- Ô nào là số đoán → đổi thành "không đủ cơ sở".
- Đối thủ nào thiếu dữ liệu đã nằm trong "Đầu vào còn thiếu" chưa.
- Nhận định có dựa trên đúng số trong bảng không; số tự tính đã ghi "(tự tính từ …)" chưa.
- Đầu file có `Trạng thái: chờ duyệt` chưa.
