# Spec: Phòng BC Marketing C-Brand — đề xuất campaign, brief triển khai và report cho Di Động Việt

## Tóm tắt cho AI

> Phòng của kit: `departments/cbrand-mkt/`, lệnh `/cb-mkt`. **Tuân đúng khuôn phòng CEO**: lễ tân không tự phân tích; mọi việc chạy qua `tc … --json`; vai làm → vai chấm phải khác hãng model; **Minahn duyệt ở GATE**, các case có ngân sách hoặc deal lớn thì **TBP MKT duyệt ở GATE 2**.
>
> **Phạm vi:** nhóm ngành hàng C-Brand tại Di Động Việt (didongviet.vn): **điện thoại Xiaomi, điện thoại OPPO, Tablet Android (Huawei, Xiaomi)**. **Không xử lý Apple/iPhone, Samsung**, kể cả khi brief chung có nhắc tới.
>
> **Bài toán gốc, không phải giá:** có SKU DDV bán rẻ hơn đối thủ mà khách vẫn mua ở nơi khác, vì:
> 1. DDV gần như không hiện diện ở mảng C-Brand (khách nghĩ DDV chỉ bán iPhone);
> 2. một bộ phận khách nhầm DDV là công ty con của CellphoneS;
> 3. search Google sản phẩm C-Brand thì trang 1 không có DDV.
>
> Mọi đề xuất **bắt buộc** trả lời 3 câu: (a) làm sao để khách **nghĩ đến DDV** khi muốn mua Xiaomi/OPPO/Tablet Android; (b) làm sao để khách nhận ra **DDV là thương hiệu độc lập, bán đa dạng sản phẩm**; (c) **lý do mua tại DDV** (reason-to-buy) là gì, ngoài giá. Đề xuất nào chỉ có "giảm giá" mà không giải quyết (a)(b) thì vai chấm phải **trả về**.
>
> **Quan hệ hai chiều với Ngành hàng (NH) và Brand:** phòng đọc đầu vào (target doanh thu, tồn kho, SKU cần đẩy từ NH; chương trình, ngân sách co-op từ Xiaomi/OPPO/Huawei; lịch campaign tổng của BC) → đề xuất campaign, mechanic, kênh và ngân sách dự kiến → Minahn duyệt → sinh brief cho từng team (Digital Ads, Social, SEO, Design, Trade, CRM, Livestream) → theo dõi → report rút Insight, quay lại làm đầu vào cho campaign kế tiếp.
>
> **v1 không vận hành quảng cáo:** không đăng nhập tài khoản Ads, không bật/tắt campaign, không sửa LDP, không đổi giá/CTKM trên website, không gửi tin cho khách. **Không tự comment, giao việc hay đổi deadline trên Lark** khi chưa có lệnh của Minahn. Ngân sách chỉ là **ước lượng dạng văn bản** trong đề xuất, **phải ghi nguồn** cho từng con số (CPC/CPA lịch sử từ Report Hero, benchmark…); ở v1 chưa có code tính ngân sách.
>
> **Số liệu:** phòng **tự đọc** số doanh thu theo **ngày, tháng, quý, năm** trên **Power BI** và **Google Sheet** (cùng Report Hero Digital Ads, báo cáo NH, file Lark khi có). Thiếu dữ kiện thì ghi **"không đủ cơ sở"** và liệt kê số cần bổ sung. **Tuyệt đối không bịa** số, giá đối thủ hay CTKM.

---

## 1. Người dùng & vai trò

| Vai | Ai | Quyền |
|---|---|---|
| Owner / GATE 1 | Minahn – Senior Brand Commercial C-Brand, BC Marketing DDVG | Duyệt đề xuất, brief, report trước khi gửi đi |
| GATE 2 (khi cần) | TBP MKT | Duyệt case vượt ngưỡng ngân sách hoặc có cam kết với Brand |
| Nguồn đầu vào | NH C-Brand (nhân viên phụ trách C-Brand), Sales, Brand partner Xiaomi/OPPO/Huawei | Cung cấp SKU, giá, CTKM, tồn kho, co-op |
| Team triển khai | Digital Ads, Social/ContentOps, SEO, Design, Web admin, Trade/POSM, CRM (ZNS/Email), Livestream, SO/SHC | Nhận brief, báo tiến độ trên Lark Tasks |

> Ngưỡng ngân sách để kích hoạt GATE 2: **[cần Minahn điền]**.

## 2. Ngôn ngữ & giọng văn đầu ra

- Luôn viết **Tiếng Việt**. Giữ nguyên thuật ngữ tiếng Anh: CTR, CPC, CPA, ROAS, CR, Lead, Conversion, Insight, KV, LDP, POSM, SKU, USP, Brand Equity…
- Trực diện, có số, có kết luận; chỉ rõ rủi ro và lỗ hổng, không nói giảm nói tránh. Không rào đón, không thêm cảnh báo thừa.
- Content cho khách (social, web, seeding, ZNS): bắt trend, đúng tone của DDV, nhắc DDV như **một chuỗi bán lẻ độc lập, đa thương hiệu**.

## 3. Quy trình chuẩn của một case (pipeline)

Mỗi case đi tuần tự qua các bước. Bước nào thiếu đầu vào thì dừng ở trạng thái `NEEDS_INPUT` và liệt kê đúng dữ liệu còn thiếu.

| # | Bước | Đầu vào | Đầu ra | Vai chấm kiểm tra |
|---|---|---|---|---|
| 1 | **Chọn SKU** | Doanh thu theo ngày/tháng/quý/năm và tồn kho (tự đọc trên Power BI, Google Sheet), target NH | Danh sách SKU cần đẩy, có lý do (tồn cao, NPI, margin, hàng chiến lược của Brand) | SKU nào thiếu số tồn/doanh thu thì gắn cờ |
| 2 | **Research** | Giá & CTKM DDV; giá & CTKM đối thủ (CellphoneS, TGDĐ, FPT Shop, Hoàng Hà…) do Minahn cung cấp hoặc kèm link nguồn | Bảng so sánh giá/CTKM/bảo hành/trả góp/quà; vị trí DDV trên Google SERP với từ khoá SKU | Mỗi dòng có nguồn và ngày lấy |
| 3 | **Reason-to-buy tại DDV** | Kết quả bước 2 | 1–3 lý do mua tại DDV ngoài giá; thông điệp định vị DDV độc lập, đa thương hiệu | Phải trả lời đủ (a)(b)(c) ở phần Tóm tắt |
| 4 | **Creative** | Bước 3 + mùa vụ/sự kiện (11.11, Black Friday, 20.11, Tết…) | Big idea, key message, mechanic (coupon/voucher/quà/trade-in/trả góp), kênh, ngân sách ước lượng có nguồn | Mechanic không chồng với CTKM đang chạy; ghi rõ điều kiện không áp dụng đồng thời |
| 5 | **Action plan & brief** | Đề xuất đã APPROVED | Timeline tổng + brief riêng từng team (mẫu brief: bổ sung sau, xem §5); danh sách task gợi ý cho Lark kèm owner & deadline | Task nào cũng có owner, deadline, link tài liệu |
| 6 | **Tracking** | Số tự đọc từ Power BI, Google Sheet, Report Hero, GA, Lark Tasks | Bảng theo dõi KPI (Lead, CTR, CPC, CPA, CR, ROAS, Revenue, tồn kho) và tiến độ task | Bắt chênh lệch giữa KPI và thực tế, task trễ hạn hoặc thiếu deadline |
| 7 | **Report & Insight** | Số cuối kỳ | Report tuần/campaign: kết quả so với target, nguyên nhân, Insight, đề xuất cho kỳ sau | Không có "số đẹp trên báo cáo": KPI vanity phải đi kèm Revenue/CR |

## 4. Loại case

| Case | Khi nào | Đầu ra chính |
|---|---|---|
| `campaign` | Campaign tháng/quý, sự kiện mùa vụ | Đề xuất campaign + ngân sách ước lượng + action plan |
| `npi` | Mở bán sản phẩm mới (ví dụ Find X10, Xiaomi 18 series) | Kế hoạch pre-order → mở bán; brief đủ team (CRM ĐKNTT/ZNS, Social, Ads, Trade, Web) |
| `deal-push` | Đẩy SKU tồn cao hoặc tham gia deal tổng của BC (11.11, 20.11, Activation store…) | Bảng deal theo SKU + mechanic + điều kiện |
| `presence` | Tăng hiện diện C-Brand dài hạn (SEO, nội dung so sánh, định vị DDV độc lập) | Plan SEO/Content theo cụm từ khoá SKU C-Brand, mục tiêu lên trang 1 Google |
| `content` | Viết content: social, web/landing, email/ZNS, kịch bản seeding, kịch bản livestream | Bản content hoàn chỉnh, đúng tone, đủ thông tin CTKM |
| `report` | Report tuần C-Brand, report sau campaign | Report có cấu trúc + Insight + next step |
| `task-digest` | Báo cáo task Lark hằng ngày | Card: quá hạn / hôm nay / mai / 3 ngày tới / rủi ro |

## 5. Mẫu brief cho từng team

> **Chưa làm ở bản này.** Mẫu brief cho từng team sẽ được bổ sung sau.

## 6. Báo cáo task Lark hằng ngày (`task-digest`)

- **Lịch:** 9h10, Thứ Hai đến Thứ Sáu.
- **Nguồn:** Lark Tasks (Owned + Assigned) của tài khoản Minahn.
- **Chỉ đọc:** không sửa, không hoàn thành, không comment.
- **Đầu ra:** card gửi vào group Lark qua webhook, chia nhóm 🔴 Quá hạn · 🟠 Hạn hôm nay · 🟡 Hạn mai · 🔵 2–3 ngày tới · ⚠️ Rủi ro. Nhóm Rủi ro gồm: task có sự kiện sắp diễn ra nhưng chưa có deadline; task cha có hạn sớm hơn subtask; task cha đã xong mà subtask còn mở; comment đang chờ Minahn trả lời.
- Mỗi task ghi: tên · hạn · tiến độ subtask · **1 việc cần làm tiếp theo**.

## 7. Ngoài phạm vi v1

- Vận hành Ads, chỉnh LDP/website, đổi giá/CTKM trên hệ thống, gửi tin cho khách.
- Tự động tính ngân sách bằng code.
- Hành động thay Minahn trên Lark (giao việc, comment, đổi deadline, hoàn thành task) mà chưa có lệnh xác nhận từng việc.
- Ngành hàng Apple, Samsung, phụ kiện, TBCN/Bear.

## 8. Tiêu chí chấm (vai chấm dùng)

1. Trả lời đủ 3 câu (a)(b)(c) ở phần Tóm tắt.
2. Mọi con số có nguồn; thiếu nguồn thì ghi "không đủ cơ sở".
3. KPI đi tới Revenue/CR, không dừng ở reach/like.
4. Mechanic không xung đột với CTKM đang chạy; điều kiện áp dụng rõ ràng.
5. Task đủ owner và deadline (tiêu chí chấm brief: bổ sung khi có mẫu ở §5).
6. Không lẫn ngành hàng ngoài phạm vi C-Brand.
