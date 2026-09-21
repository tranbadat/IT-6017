# KẾ HOẠCH BÀI TẬP LỚN — Môn "Các xu hướng công nghệ trong chuyển đổi số"
## Đề tài: Topic 1 — DGA. FANCI: Feature-based Automated NXDomain Classification and Intelligence (phát hiện botnet dùng DGA qua phân tích tên miền NXDomain)

**Nhóm:** Trần Bá Đạt · Vũ Đức Minh · Phạm Tuấn Anh · Nguyễn Đồng Hoàng
**Thời hạn:** 4 tuần | **Deliverables:** Báo cáo 15–30 trang, Slide 15–30 trang, Thuyết trình 15–20 phút (tất cả thành viên tham gia)

---

## 1. Hiểu đúng yêu cầu đầu bài

| Yêu cầu | Cách đáp ứng |
|---|---|
| Không bắt buộc phần mềm, chủ yếu tiểu luận, đọc hiểu báo cáo | Trọng tâm là phân tích, tổng hợp bài báo gốc + tài liệu liên quan |
| Thực nghiệm càng tốt (không bắt buộc) | Tuỳ chọn: minh hoạ lại 1–2 đặc trưng (feature) trên tập domain mẫu bằng Python (xem mục 6) |
| Khảo sát, tóm tắt, hướng đi | Chương 2 (Related Work) + Chương 3 (Phương pháp FANCI) |
| Đóng góp chung, kết quả | Chương 4 (Thực nghiệm & Kết quả) |
| So sánh phương pháp, cái nào tối ưu, ưu/nhược điểm | Chương 2 (bảng so sánh) + Chương 5 (đánh giá tổng hợp) |
| Tác động tới CĐS, thách thức | Chương 6 |
| Đóng góp từng thành viên — công bằng | Bảng phân công §3 + trang bìa báo cáo |
| Thuyết trình 15–20p, tất cả tham gia | Mỗi người trình bày đúng phần mình viết (~4–5p/người) |

---

## 2. Cấu trúc báo cáo (đề xuất ~24–26 trang)

1. **Mở đầu** (2 trang) — Bối cảnh botnet, C2 server, vì sao DGA ra đời, mục tiêu bài báo
2. **Cơ sở lý thuyết & Khảo sát công trình liên quan** (6–7 trang) — DGA là gì, phân loại NXD (mAGD/bNXD), khảo sát Exposure, Pleiades, Phoenix, NetFlow-based, DGArchive; bảng so sánh
3. **Phương pháp FANCI** (6–7 trang) — Kiến trúc 3 module (Training/Classification/Intelligence), 21 đặc trưng (structural/linguistic/statistical), thuật toán RF & SVM
4. **Thực nghiệm & Kết quả** (5–6 trang) — Dữ liệu (RWTH, Siemens, DGArchive), độ chính xác, khả năng tổng quát hoá, tốc độ, thử nghiệm thực tế (10 DGA mới phát hiện)
5. **Đánh giá tổng hợp** (2–3 trang) — RF vs SVM, FANCI vs các hệ thống khác, ưu/nhược điểm, phương pháp nào tối ưu và tại sao
6. **Tác động đến chuyển đổi số & Thách thức** (2–3 trang) — An toàn hạ tầng DNS trong doanh nghiệp số, triển khai dạng dịch vụ (as-a-service), thách thức (DGA né tránh, riêng tư dữ liệu, chi phí vận hành)
7. **Kết luận** (1 trang) + Tài liệu tham khảo + Phụ lục (bảng phân công, mã nguồn thực nghiệm nếu có)

---

## 3. Phân công thành viên (mỗi người phụ trách 1 chương lớn — viết báo cáo, làm slide, thuyết trình phần của mình)

| Thành viên | Phụ trách nội dung | Trang báo cáo | Slide | Thuyết trình |
|---|---|---|---|---|
| **Trần Bá Đạt** | Ch.1 Mở đầu (bối cảnh botnet, C2 server, vì sao DGA ra đời, mục tiêu bài báo) + Ch.2 Cơ sở lý thuyết & Khảo sát công trình liên quan (DGA, phân loại NXD mAGD/bNXD, Exposure, Pleiades, Phoenix, NetFlow, DGArchive, bảng so sánh) + tổng hợp/biên tập chung | ~8–9 trang | ~8 slide | ~4–5p |
| **Nguyễn Đồng Hoàng** | Ch.3 Phương pháp FANCI (kiến trúc 3 module Training/Classification/Intelligence, 21 đặc trưng structural/linguistic/statistical, RF & SVM) | ~6–7 trang | ~7 slide | ~4–5p |
| **Phạm Tuấn Anh** | Ch.4 Thực nghiệm & Kết quả (dữ liệu RWTH/Siemens/DGArchive, độ chính xác, tổng quát hoá, tốc độ, thử nghiệm thực tế — 10 DGA mới) | ~5–6 trang | ~6 slide | ~4–5p |
| **Vũ Đức Minh** | Ch.5 Đánh giá tổng hợp (RF vs SVM, ưu/nhược điểm) + Ch.6 Tác động CĐS & Thách thức + Ch.7 Kết luận | ~5–7 trang | ~6 slide | ~4–5p |

- Kết luận + Q&A: cả nhóm cùng đứng, người dẫn (Đạt) tổng kết 1 slide.
- Đóng góp được ghi rõ ở trang cuối báo cáo dưới dạng bảng (nội dung viết, số trang, vai trò trong thực nghiệm nếu có) để đảm bảo công bằng và minh bạch với giảng viên.

---

## 4. Timeline 4 tuần

### Tuần 1 — Đọc hiểu & lên khung
- Cả nhóm đọc toàn bộ bài báo FANCI 1 lượt, họp thống nhất cách hiểu chung (2h).
- Mỗi người đọc sâu phần mình phụ trách + tìm thêm 1–2 tài liệu gốc liên quan (Đạt: tìm số liệu/case study về DGA-botnet gần đây để mở đầu sinh động + đọc thêm paper Exposure/Pleiades/Phoenix nếu có bản gốc; Hoàng: đọc kỹ Random Forest/SVM cơ bản; Tuấn Anh: nghiên cứu cách trình bày bảng số liệu ACC/TPR/FPR; Minh: tìm tài liệu về an toàn DNS trong doanh nghiệp và bối cảnh chuyển đổi số cho Ch.6).
- Chốt outline chi tiết từng chương (heading cấp 2), chốt template slide.
- **Deliverable cuối tuần:** Outline báo cáo + slide khung được cả nhóm duyệt.

### Tuần 2 — Viết nội dung (draft)
- Mỗi người viết bản nháp chương của mình (ưu tiên nội dung, chưa cần đẹp).
- Đạt tổng hợp bản nháp vào 1 file chung, kiểm tra logic xuyên suốt giữa các chương.
- Bắt đầu dựng slide song song với viết báo cáo.
- **Deliverable cuối tuần:** Bản nháp đầy đủ (70–80%) của cả báo cáo và slide.

### Tuần 3 — Hoàn thiện nội dung + thực nghiệm (nếu làm)
- Hoàn thiện văn phong, số liệu, trích dẫn (theo chuẩn IEEE/APA).
- (Tuỳ chọn) Tuấn Anh/Hoàng làm thực nghiệm nhỏ minh hoạ (xem mục 6) để tăng điểm cộng.
- Review chéo: mỗi người đọc và góp ý chương của 1 người khác (đổi vòng: Đạt↔Minh, Tuấn Anh↔Hoàng).
- Hoàn thiện slide, thống nhất màu sắc/font/template.
- **Deliverable cuối tuần:** Báo cáo & slide hoàn chỉnh bản 1.0.

### Tuần 4 — Rà soát, luyện tập, nộp
- Họp tổng duyệt toàn bộ báo cáo + slide (kiểm tra số trang, format, lỗi chính tả).
- Luyện tập thuyết trình 2 lần: lần 1 từng người tự nói phần mình theo giờ, lần 2 chạy full 15–20 phút có bấm giờ, góp ý lẫn nhau.
- Chuẩn bị câu hỏi phản biện dự kiến (VD: "Vì sao FANCI không dùng deep learning?", "Điểm yếu khi DGA bắt chước từ tiếng Anh như Matsnu?").
- Hoàn thiện bảng phân công đóng góp, nộp bài.
- **Deliverable cuối tuần:** Nộp báo cáo + slide, sẵn sàng thuyết trình.

---

## 5. Nội dung cốt lõi cần có trong "So sánh phương pháp — cái nào tối ưu"

Dựa trên phần Related Work của bài báo, bảng so sánh nên có các tiêu chí: **cơ sở dữ liệu đặc trưng** (1 domain đơn lẻ vs. nhóm truy vấn), **yêu cầu theo dõi (tracking)**, **độ chính xác (ACC/TPR/FPR)**, **khả năng tổng quát hoá**, **hiệu năng/tốc độ**, **khả năng triển khai as-a-service**:

- **FANCI**: chỉ cần 1 NXD đơn lẻ, không cần tracking, ACC ~99.9%, tổng quát hoá tốt, rất nhanh (0.0025s/mẫu) → tối ưu nhất về tính nhẹ và khả năng triển khai.
- **Exposure**: cần toàn bộ traffic DNS + thông tin ngữ cảnh nhạy cảm, độ chính xác tương đương nhưng kém linh hoạt hơn.
- **Pleiades**: cần nhóm NXD theo host, ACC thấp hơn khi nhóm nhỏ.
- **Phoenix**: TPR thấp hơn FANCI đáng kể (81–95%), thiên về intelligence hơn detection.
- **NetFlow-based (Grill et al.)**: ACC dao động lớn (88–99%), phụ thuộc theo dõi luồng mạng.

→ Kết luận: FANCI tối ưu về sự đánh đổi giữa độ chính xác, hiệu năng và tính khả triển khai (do đặc trưng chỉ trích xuất từ 1 domain, không cần ngữ cảnh).

---

## 6. Gợi ý thực nghiệm nhỏ (tuỳ chọn, cộng điểm)

Không cần dựng lại toàn hệ thống FANCI. Có thể chỉ minh hoạ:
- Viết script Python trích xuất một vài đặc trưng đơn giản (độ dài domain, tỷ lệ nguyên âm, entropy Shannon, tỷ lệ ký tự lặp) trên 1 tập domain tự tạo (vài domain hợp lệ + vài domain random giả lập mAGD).
- Vẽ biểu đồ phân bố entropy/độ dài giữa 2 nhóm để trực quan hoá lý do các đặc trưng này phân biệt được domain độc hại và domain hợp lệ.
- Đây là phần "thực nghiệm" nhẹ, không cần huấn luyện RF/SVM thật, chỉ cần minh hoạ trực giác của đặc trưng — phù hợp với yêu cầu "không bắt buộc phần mềm".

---

## 7. Checklist trước khi nộp

- [ ] Báo cáo 15–30 trang, đủ 7 phần đã nêu, có trích dẫn tài liệu tham khảo
- [ ] Có bảng so sánh phương pháp + đánh giá ưu/nhược điểm rõ ràng
- [ ] Có phần tác động CĐS và thách thức
- [ ] Có bảng phân công đóng góp từng thành viên
- [ ] Slide 15–30 trang, đồng bộ template/font
- [ ] Thuyết trình 15–20 phút, đã luyện tập bấm giờ, cả 4 người đều trình bày
- [ ] Không trùng đề tài với nhóm khác (xác nhận với giảng viên nếu cần)
