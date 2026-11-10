**SERIES · HƯỚNG DẪN TỪ SỐ 0 · TẬP 2/ 7** 

# **Cài Claude, tạo phòng ban và nối công cụ cho đội AI** 

Tài liệu đi kèm video Tập 2. Làm theo từng bước dưới đây, mọi người sẽ có một **thư mục làm việc** cho đội AI làm marketing, và Claude mở được Gmail, Notion của mình. 

**Không cần biết code Khoảng 15–20 phút Máy Windows hoặc Mac** 

#### **Cần chuẩn bị** 

Một máy tính Windows hoặc Mac. 

- Một tài khoản Claude **gói Pro trở lên** . Claude Code có ở gói Pro, Max, 

- Team, Enterprise; gói Free chỉ chat, không có Claude Code. Gói Pro: 20 USD/tháng, hoặc 17 USD/tháng nếu trả theo năm (theo 

- claude.com/pricing, xem ngày 23/10/2026 — giá có thể đổi). 

- Tài khoản Gmail / Notion nếu muốn làm bước nối công cụ. 

#### **Làm xong tài liệu này, mọi người có:** 

- App Claude trên máy, mở được chế độ **Claude Code** 

- Một thư mục **phòng ban** cho đội AI, có thư mục lớn **agents** chia sẵn 3 nhân viên AI + 1 file giải thích 

- Gmail (hoặc Notion, Google Drive…) đã nối với Claude 

- Biết cách kiểm Claude đang làm việc ở đâu và dùng được công cụ gì 

Tập sau (Tập 3): viết **nội quy** cho cả đội, để AI không phải dặn lại từ đầu mỗi lần. 

**TRƯỚC KHI BẤM** 

## **Ba thứ cần nhớ** 

Cả series dùng một hình ảnh: đội AI giống một phòng ban trong công ty. 

### **Phòng ban** 

- = một thư mục trên máy 

### **Nhân viên** 

- = mỗi agent làm đúng một 

   - việc 

### **Nội quy** 

- = file luật AI đọc đầu mỗi phiên (Tập 3) 

#### **Chatbot khác agent thế nào?** 

**Chatbot:** mình hỏi, nó trả lời, xong là thôi. 

**Agent:** nhận một việc, tự làm nhiều bước, và để lại kết quả thành **file** cho mình mở ra xem. 

#### **Claude Code là gì?** 

Là Claude làm việc **ngay trong một thư mục trên máy mình** : đọc file, viết file, chạy công cụ. Mình nói tiếng Việt bình thường, nó tự lo phần kỹ thuật. 

#### **MCP / Connectors là gì?** 

MCP (Model Context Protocol) là cách để Claude **nối vào công cụ khác** như Gmail, Notion, Google Drive. Trong app Claude, chỗ bấm để nối gọi là **Connectors** . Nối rồi thì khỏi phải copy dán qua lại. 

#### **Lộ trình Tập 2** 

- **1–3** Tải, cài, mở Claude Code 

- **4–** Tạo phòng ban, kiểm tra, chia nhân **6** viên 

- **7–8** Nối Gmail / Notion, hỏi thử 

**Mẹo cho người mới:** làm lần lượt, mỗi bước thấy đúng kết quả ở ô xanh "Bạn sẽ thấy" rồi mới qua bước sau. Tên nút trong tài liệu lấy từ app lúc em quay (10/2026); app cập nhật có thể đổi chữ một chút, vị trí thường vẫn vậy. 

solomi · Hướng dẫn từ số 0 · Tập 2 

2 

**PHẦN A · CÀI ĐẶT** 

## **Tải Claude và tạo phòng ban** 

### **1** 

#### **Tải app Claude** 

Mở trình duyệt (vd Chrome), tìm **"Claude for desktop"** , vào trang tải chính thức của Claude. Máy Windows chọn Windows, máy Mac chọn macOS. 

**claude.com/download → Windows · Download hoặc macOS · Download** 

Chỉ tải từ trang của Claude, không tải từ trang lạ. 



<!-- Start of picture text -->
2<br><!-- End of picture text -->

#### **Cài, đăng nhập, mở app** 

Mở file vừa tải, cài như phần mềm bình thường. Đăng nhập tài khoản Claude (gói Pro trở lên), rồi mở app từ thanh taskbar (Windows) hoặc Dock (Mac). 



<!-- Start of picture text -->
3<br><!-- End of picture text -->

#### **Chuyển sang Claude Code** 

Màn hình đầu tiên là giao diện **chat** , hỏi đáp như bình thường. Bấm nút **Code** ở góc trên bên trái để sang **Claude Code** — chế độ agent làm việc trong thư mục trên máy. 

**Chat → Code (góc trên trái)** 

**Bạn sẽ thấy:** giao diện Claude Code với ô chat ở giữa, dưới ô chat có chữ **This computer** . 

**4** 

#### **Tạo phòng ban (một thư mục mới)** 

**Choose → Open folder → chuột phải · New · Folder → đặt tên → Select Folder →** 

##### **Trust workspace** 

- Ở dưới ô chat, cạnh chữ **This computer** , bấm **Choose** rồi chọn **Open folder** . 

- Chọn chỗ mình hay lưu tài liệu (vd Documents). Chuột phải → **New** → **Folder** . 

- Đặt tên **không dấu, không dấu cách** , vd **marketing_ai_agent_team** . 

- Chọn thư mục đó, bấm **Select Folder** . App hỏi có tin thư mục này không → bấm **Trust workspace** . 

**Vì sao không dấu, không dấu cách?** Tên có dấu hoặc dấu cách dễ làm công cụ chạy lỗi về sau. Dùng gạch dưới **_** thay cho dấu cách. 

solomi · Hướng dẫn từ số 0 · Tập 2 

3 

**PHẦN B · KIỂM TRA VÀ CHIA NHÂN VIÊN** 

## **Phòng ban đã sẵn sàng chưa?** 

**5** 

#### **Kiểm tra Claude đang làm việc ở đâu** 

Dán câu này vào ô chat rồi gửi: 

###### **CÂU LỆNH · CHÉP NGUYÊN** 

Bạn đang làm việc trong thư mục nào? Trong đó đang có gì? 

**Bạn sẽ thấy:** Claude trả lời đúng tên thư mục vừa tạo (vd marketing_ai_agent_team) và báo thư mục đang **trống** . 

Nếu nó báo một thư mục khác → quay lại bước 4 chọn lại thư mục. Mọi việc ở các bước sau đều làm trong thư mục này. 

**6** 

#### **Chia nhân viên cho phòng ban** 

Dán câu lệnh này. Claude tạo một thư mục lớn **agents** , bên trong là các nhân viên AI nhỏ, cộng một file giải thích: 

###### **CÂU LỆNH · CHÉP NGUYÊN** 

Hãy dựng khung cho đội AI làm marketing của tôi ngay trong thư mục này. Tạo một thư mục lớn tên agents. Bên trong agents tạo 3 thư mục con, mỗi thư mục là một nhân viên AI: research (nghiên cứu khách hàng, đối thủ, xu hướng), content (viết bài, kịch bản), reports (số liệu, bài nào hiệu quả). Ở ngoài cùng tạo một file README.md viết bằng tiếng Việt dễ hiểu, giải thích mỗi thư mục dùng để làm gì. Chưa tạo nội quy hay hướng dẫn cho từng nhân viên. Làm xong thì vẽ lại cây thư mục cho tôi xem. 

**Bạn sẽ thấy** (kết quả lần chạy thử của em, 24/10/2026): 

```
marketing_ai_agent_team/
├── README.md         ← file giải thích
└── agents/           ← thư mục lớn: cả đội AI
    ├── research/     ← nhân viên Nghiên cứu
    ├── content/      ← nhân viên Nội dung
    └── reports/      ← nhân viên Báo cáo
```

|**Thư mục**|**Dùng để**|
|---|---|
|agents|thư mục lớn chứa cả đội; mỗi thư mục con là một nhân viên AI|
|agents/research|nghiên cứu khách hàng, đối thủ, xu hướng|
|agents/content|viết bài, kịch bản|
|agents/reports|số liệu, bài nào hiệu quả|



Mỗi lần chạy, câu chữ trong README có thể khác một chút — chỉ cần có thư mục agents chứa 3 nhân viên và 1 file README là đúng. 

solomi · Hướng dẫn từ số 0 · Tập 2 

4 

**PHẦN C · NỐI CÔNG CỤ** 

## **Cho nhân viên AI dùng Gmail, Notion** 

**7** 

#### **Nối một công cụ qua Connectors** 

**dấu + ở ô chat → Connectors → Manage connectors → + cạnh Gmail → chọn tài khoản Google → đọc quyền · Continue → Connected** 

- Bấm **dấu cộng** ở ô chat, chọn **Connectors** , rồi **Manage connectors** . Ở đây có sẵn Gmail, Notion, Google Drive, Canva… 

- Bấm dấu cộng cạnh **Gmail** , chọn tài khoản Google. 

- **Đọc kỹ nó xin những quyền gì** , đồng ý thì bấm **Continue** . 

- Hiện chữ **Connected** là xong. Quay lại app, Gmail có dấu tích. 

Notion, Google Drive, Canva… làm y như vậy. 

**8** 

#### **Hỏi thử xem Claude dùng được gì** 

###### **CÂU LỆNH · CHÉP NGUYÊN** 

Bạn đang kết nối được những công cụ nào? Với mỗi công cụ, liệt kê ngắn những việc bạn làm được trong đó. 

**Bạn sẽ thấy:** Claude báo tên các công cụ đã nối (vd Gmail, Notion) và danh sách việc nó làm được trong từng công cụ. Lúc em quay, Notion có 65 công cụ, Gmail có 23 — số này tuỳ phiên bản, không cần giống. 

Muốn thử Gmail thật mà an toàn, dùng câu chỉ đọc: 

###### **CÂU LỆNH · CHÉP NGUYÊN** 

Đọc 5 email mới nhất trong Gmail của tôi và tóm tắt mỗi email một dòng. Không trả lời, không xoá, không gửi gì. 

**Lưu ý an toàn:** nối Gmail là Claude đọc được thư của mình. Ở Tập 3 mình sẽ ghi vào nội quy: **không tự gửi, không tự xoá, không trả lời khi chưa hỏi mình** . Trước khi có nội quy, mỗi câu lệnh liên quan tới Gmail nên tự ghi rõ "không gửi, không xoá". 

solomi · Hướng dẫn từ số 0 · Tập 2 

5 

**KHI BỊ KẸT** 

## **Lỗi hay gặp và cách sửa** 

|**Gặp chuyện gì**|**Làm gì**|
|---|---|
|Không thấy nút**Code**|Kiểm gói tài khoản: Claude Code chỉ có ở gói Pro trở lên. Cập nhật<br>app lên bản mới nhất rồi mở lại.|
|Claude báo sai thư mục ở bước 5|Bấm Choose→Open folder chọn lại đúng thư mục, rồi hỏi lại câu<br>bước 5.|
|Bấm Select mà không có gì xảy ra|Bấm chọn (tô sáng) thư mục trước, rồi mới bấm Select Folder.|
|Claude tạo thư mục ở chỗ khác|Bạn đang mở nhầm thư mục. Làm lại bước 4–5 trước khi chạy câu<br>lệnh bước 6.|
|Không thấy Gmail / Notion trong<br>Connectors|Tìm trong ô tìm kiếm của Manage connectors; tên chữ có thể khác<br>theo phiên bản app.|
|Nối xong mà Claude bảo không<br>dùng được|Mở một phiên chat mới trong cùng thư mục rồi hỏi lại câu bước 8.|



#### **AI có thể sai ở đâu, bạn kiểm chỗ nào** 

- **Thư mục:** luôn hỏi câu bước 5 trước khi giao việc — sai thư mục thì mọi file nằm sai chỗ. 

- **Cây thư mục:** mở thư mục trên máy ra xem tận mắt, đừng chỉ tin câu trả lời trong chat. 

- **Công cụ đã nối:** Claude có thể kể thiếu hoặc kể chung chung — thử một câu chỉ đọc (bước 8) để chắc nó dùng được thật. 

#### **Tóm tắt Tập 2** 

   - Tải app ở claude.com/download, đăng nhập gói Pro trở lên 

   - Chat → Code: chuyển sang Claude Code 

   - Choose → Open folder → tạo thư mục không dấu → Select Folder → Trust workspace Hỏi "Bạn đang làm việc trong thư mục nào?" để kiểm 

   - Dán câu lệnh tạo agents với 3 nhân viên (research, content, reports) + README 

   - Dấu + → Connectors → Manage connectors → nối Gmail / Notion → hỏi thử 

- Tập 3: viết nội quy cho cả đội — Claude sẽ phỏng vấn mọi người từng câu để tự viết. 

solomi · @_solouniverse · Hướng dẫn từ số 0 · Tập 2 

6 

