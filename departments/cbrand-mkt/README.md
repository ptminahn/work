# Phòng BC Marketing C-Brand

Đội AI hỗ trợ Minahn đề xuất campaign, viết brief, content và report cho **Xiaomi, OPPO, Tablet Android (Huawei, Xiaomi)** tại Di Động Việt.

## Dùng thế nào

Mở Claude Code trong thư mục repo `work`, gõ lệnh `/cb-mkt` kèm yêu cầu bằng tiếng Việt:

| Muốn làm | Gõ |
|---|---|
| Đề xuất campaign | `/cb-mkt Đề xuất campaign Black Friday cho Xiaomi 15T, file doanh thu và tồn ở du-lieu/` |
| Mở bán sản phẩm mới | `/cb-mkt Kế hoạch NPI OPPO Find X10, mở bán 01/12` |
| Đẩy hàng tồn | `/cb-mkt Deal 12.12 đẩy tồn Redmi Pad` |
| Tăng hiện diện trên Google | `/cb-mkt Plan presence để DDV lên trang 1 với từ khoá "xiaomi 15t"` |
| Viết content | `/cb-mkt Viết 3 post Facebook cho OPPO Reno14, CTKM: …` |
| Report tuần | `/cb-mkt Report tuần 45 C-Brand, số ở du-lieu/` |
| Xem các case | `/cb-mkt trang-thai` |
| Duyệt | `/cb-mkt duyet <case_id>` |
| Trả về sửa | `/cb-mkt tra-ve <case_id> <góp ý>` |
| Đã bổ sung số, chạy tiếp | `/cb-mkt tiep <case_id>` |

Kết quả nằm trong `cases/<case_id>/`, mỗi bước một file, kết quả chấm ở `cases/<case_id>/cham/`.

## Đội có những ai

| Agent | Làm gì |
|---|---|
| `/cb-mkt` (lễ tân) | Nhận yêu cầu, mở case, gọi đúng người, dừng chờ duyệt. Không tự phân tích |
| `cb-sku` | Bước 1: chọn SKU cần đẩy từ doanh thu, tồn kho |
| `cb-research` | Bước 2: so giá, CTKM đối thủ, vị trí DDV trên Google |
| `cb-strategy` | Bước 3–4: Reason-to-buy, Big idea, mechanic, kênh, ngân sách ước lượng |
| `cb-plan` | Bước 5: timeline, brief từng team, task gợi ý cho Lark |
| `cb-report` | Bước 6–7: tracking, report, Insight; task digest |
| `cb-content` | Content social, web, ZNS, seeding, livestream |
| `cb-review` | Vai chấm: chấm mọi đầu ra, chạy model khác vai làm |

## File quan trọng

| File | Nội dung |
|---|---|
| `SPEC.md` | Spec gốc |
| `NOI_QUY.md` | Luật mọi agent phải theo |
| `QUY_TRINH.md` | Pipeline 7 bước, loại case, trạng thái, GATE |
| `TIEU_CHI_CHAM.md` | Tiêu chí vai chấm dùng |
| `cau-hinh.md` | **Minahn điền:** ngưỡng GATE 2, link Power BI / Sheet / Report Hero |
| `mau/` | Mẫu đầu ra từng bước |
| `du-lieu/` | Thả file số liệu (export Power BI, Report Hero, báo cáo NH…) |
| `cases/` | Hồ sơ từng case |

## Cần làm trước khi dùng

1. Điền **ngưỡng GATE 2** và các link nguồn trong `cau-hinh.md`.
2. Nối **Google Drive** trong Connectors để agent đọc Google Sheet.
3. Power BI chưa có connector: export số ra CSV/XLSX, thả vào `du-lieu/`.

## Giới hạn của bản v1

- Không chạy Ads, không sửa website, không gửi tin cho khách, không thao tác Lark.
- Ngân sách chỉ là ước lượng bằng chữ, có nguồn từng số, chưa có công cụ tính.
- Mẫu brief chuẩn cho từng team chưa có (SPEC §5). Đang dùng khung tạm.
- `task-digest` chưa chạy được vì chưa nối Lark. Tạm thời export task vào `du-lieu/`.
- Vai chấm khác **model** (opus) với vai làm (sonnet), chưa khác **hãng** như spec gốc.
- Chưa dùng khuôn "phòng CEO" và công cụ `tc … --json` của spec, vì repo chưa có. Có kit thì ráp lại.
- `cases/` và `du-lieu/` **không được đẩy lên GitHub** (đã `.gitignore`) vì repo đang public.
