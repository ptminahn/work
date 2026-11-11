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
| Chê và ghi luật mới | `/cb-mkt che <case_id> research <sai ở đâu> \| <sửa thành gì> \| <luật một câu>` |
| Research nhanh vài SKU | `/cb-mkt Research Xiaomi 15T và Pad 7, từ khoá "xiaomi 15t", số ở du-lieu/` |

Kết quả nằm trong `cases/<case_id>/`, mỗi bước một file, kết quả chấm ở `cases/<case_id>/cham/`.

## Đội có những ai

Làm theo khoá học: **mở từng phòng, chạy ổn rồi mới mở tiếp**. Mỗi phòng có bản mô tả công việc `agents/<phòng>/VAI_TRO.md` 5 phần: NHẬN · LÀM · GIAO · LUẬT · TỰ KIỂM.

| Phòng | Làm gì | Trạng thái |
|---|---|---|
| Lễ tân `/cb-mkt` | Nhận yêu cầu, mở case, gọi đúng phòng, ghi file chấm, dừng chờ duyệt | Đang mở |
| Research | So giá, CTKM đối thủ, vị trí DDV trên Google | **Đang mở** |
| Chấm | Người kiểm, chỉ được đọc, model khác phòng làm | **Đang mở** |
| Chọn SKU | Chọn SKU cần đẩy từ doanh thu, tồn kho | Chưa mở |
| Chiến lược | Reason-to-buy, Big idea, mechanic, ngân sách ước lượng | **Đang mở** |
| Report | Tracking, report, Insight; task digest | Chưa mở |
| Content | Social, web, ZNS, seeding, livestream | Chưa mở |
| Kế hoạch | Timeline, brief từng team, task gợi ý cho Lark | **Đang mở** |

Mở phòng: sửa dòng trạng thái trong `VAI_TRO.md` của phòng đó và bảng ở `QUY_TRINH.md` mục 1.

## Cách làm cho đội tốt dần lên

Chạy → đọc file → chê 3 phần (sai ở đâu · sửa thành gì · luật một câu) → luật được ghi vào `VAI_TRO.md` có ngày → `/clear` rồi chạy lại. Chê trong chat thì phiên sau quên; ghi vào file thì lần nào phòng cũng đọc lại.

## File quan trọng

| File | Nội dung |
|---|---|
| `SPEC.md` | Spec gốc |
| `../../CLAUDE.md` | Nội quy chung 6 phần, cả đội đọc đầu mỗi phiên |
| `NOI_QUY.md` | Luật riêng phòng C-Brand: 3 câu (a)(b)(c), số liệu, GATE |
| `agents/<phòng>/VAI_TRO.md` | Mô tả công việc từng phòng, nơi ghi luật mới |
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
