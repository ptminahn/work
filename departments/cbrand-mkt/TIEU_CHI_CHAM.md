# Tiêu chí chấm (vai chấm `cb-review` dùng)

Chấm từng tiêu chí: `ĐẠT` / `KHÔNG ĐẠT` / `KHÔNG ÁP DỤNG`. Có **bất kỳ** tiêu chí nào `KHÔNG ĐẠT` thì kết luận `TRA_VE`.

## Tiêu chí chung (mọi bước)

| # | Tiêu chí | Cách kiểm |
|---|---|---|
| C1 | Trả lời đủ **(a)(b)(c)** | Áp dụng cho bước 3, 4 và case `presence`, `npi`, `campaign`. Mỗi câu phải có câu trả lời cụ thể, gắn với kênh/hành động, không phải khẩu hiệu. Chỉ có "giảm giá" mà không giải quyết (a)(b) → KHÔNG ĐẠT |
| C2 | Mọi con số có nguồn | Quét từng số (giá, doanh thu, tồn, CPC, CPA, ROAS, ngân sách, thứ hạng SERP). Số nào thiếu `[nguồn: …]` → KHÔNG ĐẠT, liệt kê số đó. Số không có nguồn mà không ghi "không đủ cơ sở" → nghi bịa, ghi rõ |
| C3 | KPI đi tới Revenue / CR | KPI vanity (reach, view, like, CTR) đứng một mình → KHÔNG ĐẠT |
| C4 | Mechanic không xung đột CTKM đang chạy | Có ghi CTKM đang chạy (kèm nguồn) và điều kiện "không áp dụng đồng thời" rõ ràng. Áp dụng bước 4, `deal-push` |
| C5 | Task đủ owner, deadline, link tài liệu | Áp dụng bước 5. Tiêu chí chấm brief chi tiết: bổ sung khi có mẫu brief |
| C6 | Không lẫn ngành hàng ngoài C-Brand | Có Apple/iPhone, Samsung, phụ kiện, TBCN/Bear trong phần đề xuất → KHÔNG ĐẠT |
| C7 | Đúng điều cấm và cổng duyệt | Dòng đầu có `Trạng thái: chờ duyệt`. Không có từ cấm ("rẻ nhất", "giá tốt nhất" khi chưa có số), không hứa doanh thu/ngày giao với khách, không bịa đánh giá. Theo `CLAUDE.md` mục 5 |

## Tiêu chí riêng theo bước

| Bước | Kiểm thêm |
|---|---|
| 1 – SKU | Mỗi SKU có lý do chọn (tồn cao, NPI, margin, hàng chiến lược Brand). SKU thiếu số tồn hoặc doanh thu phải được **gắn cờ** |
| 2 – Research | Mỗi dòng giá/CTKM có nguồn **và ngày lấy**. Có vị trí DDV trên Google SERP theo từ khoá SKU, hoặc ghi "không đủ cơ sở" |
| 3 – RTB | 1–3 lý do mua ngoài giá, mỗi lý do có bằng chứng từ bước 2. Có thông điệp định vị DDV độc lập, đa thương hiệu |
| 4 – Creative | Có Big idea, key message, mechanic, kênh, ngân sách ước lượng. Ngân sách từng dòng có cơ sở. Có nêu GATE 2 nếu vượt ngưỡng hoặc có cam kết Brand |
| 5 – Plan | Timeline tổng, task theo team; không task nào thiếu owner/deadline |
| 6 – Tracking | Bắt chênh lệch KPI vs thực tế; nêu task trễ hạn hoặc thiếu deadline |
| 7 – Report | So với target, nêu nguyên nhân, Insight, đề xuất kỳ sau. Không "số đẹp trên báo cáo" |
| content | Đúng tone DDV, thể hiện DDV độc lập đa thương hiệu, thông tin CTKM khớp nguồn, có điều kiện áp dụng |

## Mẫu file chấm

Phòng Chấm chỉ được đọc, trả nội dung này cho lễ tân; lễ tân ghi vào `cham/<buoc>-v<n>.md`:

```markdown
# Chấm: <buoc> – vòng <n>

- File chấm: <đường dẫn>
- Kết luận: PASS | TRA_VE
- Cần GATE 2: Có | Không | Chưa xác định (lý do)

| # | Tiêu chí | Kết quả | Ghi chú |
|---|---|---|---|
| C1 | (a)(b)(c) | ĐẠT/KHÔNG ĐẠT/KHÔNG ÁP DỤNG | … |
| … | | | |

## Lỗi phải sửa (nếu TRA_VE)
1. <vị trí> – <lỗi> – <yêu cầu sửa cụ thể>

## Rủi ro / lỗ hổng cần Minahn biết
- …
```
