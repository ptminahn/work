# Quy trình vận hành phòng C-Brand

## 1. Các vai

| Vai | Agent | Việc | Model |
|---|---|---|---|
| Lễ tân | lệnh `/cb-mkt` (phiên chính) | Nhận yêu cầu, phân loại case, mở thư mục case, gọi đúng vai làm, gọi vai chấm, dừng ở GATE. **Không tự phân tích, không tự viết nội dung.** | model của phiên |
| Vai làm: SKU | `cb-sku` | Bước 1 – Chọn SKU | sonnet |
| Vai làm: Research | `cb-research` | Bước 2 – Research giá, CTKM, SERP | sonnet |
| Vai làm: Chiến lược | `cb-strategy` | Bước 3 – Reason-to-buy; Bước 4 – Creative, mechanic, kênh, ngân sách ước lượng | sonnet |
| Vai làm: Kế hoạch | `cb-plan` | Bước 5 – Action plan, timeline, brief, task Lark gợi ý | sonnet |
| Vai làm: Report | `cb-report` | Bước 6 – Tracking; Bước 7 – Report & Insight; `task-digest` | sonnet |
| Vai làm: Content | `cb-content` | Case `content` | sonnet |
| Vai chấm | `cb-review` | Chấm mọi đầu ra theo `TIEU_CHI_CHAM.md` | **opus** (khác model vai làm) |

> Spec gốc yêu cầu vai chấm **khác hãng** model với vai làm. Claude Code chỉ chạy model Claude, nên v1 dùng **khác model** (vai làm sonnet, vai chấm opus). Muốn khác hãng thật thì cần thêm công cụ ngoài, để sang bản sau.

## 2. Pipeline 7 bước

| # | Bước | Vai làm | File đầu ra trong case |
|---|---|---|---|
| 1 | Chọn SKU | `cb-sku` | `01-sku.md` |
| 2 | Research | `cb-research` | `02-research.md` |
| 3 | Reason-to-buy tại DDV | `cb-strategy` | `03-rtb.md` |
| 4 | Creative | `cb-strategy` | `04-creative.md` |
| 5 | Action plan & brief | `cb-plan` | `05-plan.md` |
| 6 | Tracking | `cb-report` | `06-tracking.md` |
| 7 | Report & Insight | `cb-report` | `07-report.md` |

Bước sau chỉ chạy khi bước trước đã `PASS` ở vai chấm. Bước 5 chỉ chạy khi đề xuất (bước 1–4) đã **APPROVED ở GATE 1** (và GATE 2 nếu cần).

## 3. Loại case và các bước chạy

| Case | Khi nào | Bước chạy | Dừng ở GATE sau bước |
|---|---|---|---|
| `campaign` | Campaign tháng/quý, sự kiện mùa vụ | 1 → 2 → 3 → 4 ‖ GATE → 5 | 4 và 5 |
| `npi` | Mở bán sản phẩm mới | 1 → 2 → 3 → 4 ‖ GATE → 5 (pre-order → mở bán, đủ team CRM ĐKNTT/ZNS, Social, Ads, Trade, Web) | 4 và 5 |
| `deal-push` | Đẩy SKU tồn cao, deal tổng của BC | 1 → 2 → 4 (bảng deal theo SKU + mechanic + điều kiện) | 4 |
| `presence` | Tăng hiện diện C-Brand dài hạn | 2 (SERP theo cụm từ khoá) → 3 → 4 (plan SEO/Content) | 4 |
| `content` | Viết content cho khách | `cb-content` → `content.md` | content |
| `report` | Report tuần / sau campaign | 6 → 7 | 7 |
| `task-digest` | Báo cáo task Lark hằng ngày | `cb-report` → `digest.md` | — (chỉ đọc) |

## 4. Trạng thái case

Ghi ở đầu `case.md`, trường `trang_thai`:

| Trạng thái | Nghĩa |
|---|---|
| `NEEDS_INPUT` | Thiếu đầu vào. `case.md` liệt kê đúng dữ liệu còn thiếu và lấy ở đâu |
| `IN_PROGRESS` | Vai làm đang chạy bước `buoc_hien_tai` |
| `IN_REVIEW` | Vai chấm đang chấm |
| `RETURNED` | Vai chấm trả về; vai làm sửa (tối đa 2 vòng, quá 2 vòng thì dừng và báo Minahn) |
| `WAITING_GATE1` | Chờ Minahn duyệt |
| `WAITING_GATE2` | Chờ TBP MKT duyệt (Minahn ghi kết quả) |
| `APPROVED` | Đã duyệt. Chỉ ghi khi Minahn ra lệnh |
| `DONE` | Case đóng |

## 5. Cấu trúc một case

```
cases/<YYYYMMDD>-<loai>-<slug>/
├── case.md            ← trạng thái, yêu cầu gốc, đầu vào còn thiếu, nhật ký
├── 01-sku.md … 07-report.md   (tuỳ loại case)
└── cham/
    ├── 01-sku-v1.md   ← kết quả chấm từng bước, từng vòng
    └── …
```

Ví dụ: `cases/20261110-campaign-black-friday-xiaomi/`.

## 6. Vòng làm – chấm

1. Lễ tân gọi vai làm, đưa đường dẫn case và bước cần làm.
2. Vai làm đọc `NOI_QUY.md`, `cau-hinh.md`, `case.md`, các bước trước, mẫu trong `mau/`, rồi ghi file bước.
3. Thiếu đầu vào: vai làm ghi phần "Đầu vào còn thiếu" và trả về `NEEDS_INPUT`. Lễ tân dừng, báo Minahn đúng danh sách đó.
4. Lễ tân gọi `cb-review` chấm file bước. Kết quả ghi vào `cham/<buoc>-v<n>.md`.
5. `TRA_VE` → lễ tân gửi lại vai làm kèm file chấm. Tối đa 2 vòng.
6. `PASS` → sang bước tiếp, hoặc dừng ở GATE nếu bước đó có GATE.
