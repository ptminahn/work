# Quy trình vận hành phòng C-Brand

## 1. Các phòng và trạng thái

Mở từng phòng, chạy ổn (qua vài vòng chê-sửa với số thật) rồi mới mở phòng tiếp. Mở phòng = đổi dòng trạng thái trong `VAI_TRO.md` của phòng đó và cập nhật bảng dưới.

| Phòng | Mô tả công việc | Agent | Model | Trạng thái |
|---|---|---|---|---|
| Lễ tân | `.claude/commands/cb-mkt.md` | phiên chính | model của phiên | ĐANG MỞ |
| Research | `agents/research/VAI_TRO.md` | `cb-research` | sonnet | **ĐANG MỞ** (2026-11-11) |
| Chấm | `agents/cham/VAI_TRO.md` | `cb-review` | **opus**, chỉ đọc | **ĐANG MỞ** (2026-11-11) |
| Chọn SKU | `agents/sku/VAI_TRO.md` | `cb-sku` | sonnet | CHƯA MỞ |
| Chiến lược | `agents/chien-luoc/VAI_TRO.md` | `cb-strategy` | sonnet | CHƯA MỞ |
| Kế hoạch | `agents/ke-hoach/VAI_TRO.md` | `cb-plan` | sonnet | CHƯA MỞ |
| Report | `agents/report/VAI_TRO.md` | `cb-report` | sonnet | CHƯA MỞ |
| Content | `agents/content/VAI_TRO.md` | `cb-content` | sonnet | CHƯA MỞ |

Thứ tự mở đề xuất: Research + Chấm → Chọn SKU → Chiến lược → Report → Content → Kế hoạch.

> Spec gốc yêu cầu phòng Chấm **khác hãng** model với phòng làm. Claude Code chỉ chạy model Claude, nên v1 dùng **khác model** (phòng làm sonnet, phòng Chấm opus).

## 2. Pipeline 7 bước

| # | Bước | Phòng | File đầu ra trong case |
|---|---|---|---|
| 1 | Chọn SKU | Chọn SKU | `01-sku.md` |
| 2 | Research | Research | `02-research.md` |
| 3 | Reason-to-buy tại DDV | Chiến lược | `03-rtb.md` |
| 4 | Creative | Chiến lược | `04-creative.md` |
| 5 | Action plan & brief | Kế hoạch | `05-plan.md` |
| 6 | Tracking | Report | `06-tracking.md` |
| 7 | Report & Insight | Report | `07-report.md` |

Bước sau chỉ chạy khi bước trước đã `PASS` ở phòng Chấm. Bước 5 chỉ chạy khi đề xuất (bước 1–4) đã **APPROVED ở GATE 1** (và GATE 2 nếu cần).

## 3. Loại case và các bước chạy

| Case | Khi nào | Bước chạy | Dừng ở GATE sau bước |
|---|---|---|---|
| `research` | Minahn đưa SKU/từ khoá, cần bảng so sánh và SERP | 2 | 2 |
| `campaign` | Campaign tháng/quý, sự kiện mùa vụ | 1 → 2 → 3 → 4 ‖ GATE → 5 | 4 và 5 |
| `npi` | Mở bán sản phẩm mới | 1 → 2 → 3 → 4 ‖ GATE → 5 | 4 và 5 |
| `deal-push` | Đẩy SKU tồn cao, deal tổng của BC | 1 → 2 → 4 | 4 |
| `presence` | Tăng hiện diện C-Brand dài hạn | 2 → 3 → 4 | 4 |
| `content` | Viết content cho khách | Content | content |
| `report` | Report tuần / sau campaign | 6 → 7 | 7 |
| `task-digest` | Báo cáo task Lark hằng ngày | Report | — (chỉ đọc) |

Case cần phòng **CHƯA MỞ**: lễ tân chạy tới hết phần các phòng đang mở làm được, rồi dừng và báo phòng nào cần mở tiếp. Không tự làm thay phòng chưa mở.

## 4. Trạng thái case

| Trạng thái | Nghĩa |
|---|---|
| `NEEDS_INPUT` | Thiếu đầu vào; `case.md` liệt kê đúng dữ liệu còn thiếu |
| `IN_PROGRESS` | Phòng làm đang chạy `buoc_hien_tai` |
| `IN_REVIEW` | Phòng Chấm đang chấm |
| `RETURNED` | Phòng Chấm trả về; phòng làm sửa (tối đa 2 vòng) |
| `BLOCKED_PHONG` | Bước tiếp theo thuộc phòng chưa mở |
| `WAITING_GATE1` | Chờ Minahn duyệt |
| `WAITING_GATE2` | Chờ TBP MKT duyệt |
| `APPROVED` | Đã duyệt (chỉ khi Minahn ra lệnh) |
| `DONE` | Case đóng |

## 5. Cấu trúc một case

```
cases/<YYYYMMDD>-<loai>-<slug>/
├── case.md            ← trạng thái, yêu cầu gốc, đầu vào còn thiếu, nhật ký
├── 01-sku.md … 07-report.md   (tuỳ loại case)
└── cham/<buoc>-v<n>.md        ← lễ tân ghi từ kết quả phòng Chấm
```

## 6. Vòng làm – chấm

1. Lễ tân gọi phòng làm, đưa đường dẫn case và bước.
2. Phòng làm đọc nội quy, `VAI_TRO.md`, `case.md`, bước trước, mẫu; ghi file bước với `Trạng thái: chờ duyệt`.
3. `NEEDS_INPUT` → lễ tân dừng, báo Minahn đúng danh sách thiếu.
4. Lễ tân gọi phòng Chấm (chỉ đọc). Phòng Chấm trả nội dung; **lễ tân ghi** ra `cham/<buoc>-v<n>.md`.
5. `TRA_VE` → lễ tân gửi lại phòng làm kèm file chấm. Tối đa 2 vòng.
6. `PASS` → bước tiếp, hoặc dừng ở GATE.

## 7. Vòng chê → ghi luật → chạy lại (cách đội tốt dần lên)

Khi Minahn đọc file và thấy sai, chê theo 3 phần:

1. **Sai ở đâu:** đúng dòng, đúng lỗi.
2. **Sửa thành gì:** nói rõ muốn thế nào.
3. **Ghi vào file:** luật một câu, ghi vào mục "Luật thêm" của `VAI_TRO.md` phòng đó, kèm ngày. Luật chung cả đội thì ghi vào `CLAUDE.md`.

Gõ: `/cb-mkt che <case_id> <phòng> <sai ở đâu> | <sửa thành gì> | <luật một câu>`. Lễ tân ghi luật vào file, cho phòng sửa file case, rồi chạy lại phòng Chấm. Muốn chắc luật có tác dụng: mở phiên mới (`/clear`) rồi chạy lại case.

Phòng Chấm bỏ sót lỗi → chê phòng Chấm theo đúng cách trên, ghi luật vào `agents/cham/VAI_TRO.md`.
