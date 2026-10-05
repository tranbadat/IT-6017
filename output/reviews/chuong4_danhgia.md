# Đánh giá tính đúng đắn của Chương 4

Ngày rà soát: 05/10/2026. Phạm vi: Chương 4, phần phụ lục mã nguồn và thực nghiệm minh họa trong repository.

## Kết luận

Chương 4 phù hợp làm **chương tổng hợp và phân tích thực nghiệm của một tiểu luận đọc hiểu FANCI**, kèm minh họa đặc trưng có thể tái tạo. Các số liệu chính khớp bài báo gốc; các công thức và phép quy đổi đã kiểm tra đúng. Sau đợt rà soát này, những câu dễ gây hiểu quá mức đã được chỉnh trực tiếp trong bản LaTeX.

Mức xác minh cần được phân biệt:

| Nội dung | Kết quả đánh giá | Mức bằng chứng |
|---|---|---|
| Số liệu ở các bảng 4.1, 4.3–4.8 | Khớp công bố, không phát hiện ô bị chép sai | Đối chiếu bài báo, chưa tính lại từ dữ liệu gốc |
| Công thức ACC, TPR, TNR, FPR, FNR và precision theo tỷ lệ lớp | Đúng với các điều kiện được nêu | Kiểm tra toán học |
| Dữ liệu RWTH và Siemens | Tác giả công bố là bản ghi DNS thực năm 2017 | Nhóm chưa trực tiếp thu thập hoặc kiểm toán dữ liệu đó |
| Kho DGArchive | Nguồn mAGD sinh từ DGA đã dịch ngược, theo mô tả của tác giả | Nhãn theo thuật toán sinh; không chứng minh mọi miền là C2 đang hoạt động |
| Thực nghiệm 360 mẫu ở Mục 4.9 | Đúng, tái tạo được | Chạy lại mã và tính lại độc lập từ CSV |
| Hiệu quả trên mạng hiện nay | Chưa được đánh giá trong dự án | Không có bản ghi mạng mới hoặc mô hình FANCI được tái lập |
| Văn phong và giới hạn suy luận | Đã chỉnh những chỗ thiếu điều kiện hoặc dễ hiểu sai | Phân biệt kết quả công bố, phép tính của nhóm và minh họa tổng hợp |

Nguồn chính: [Schüppen và cộng sự, FANCI, USENIX Security 2018](https://www.usenix.org/system/files/conference/usenixsecurity18/sec18-schuppen.pdf), Mục 5 và Phụ lục A/B. Báo cáo này đánh giá độ khớp với công bố, không xác nhận độc lập rằng mọi kết quả công bố đều được tái lập.

## Dữ liệu có thực tế không?

- **RWTH/Siemens:** có căn cứ từ dữ liệu mạng thực được mô tả trong bài báo. Chương 4 đã ghi rõ nguồn, năm thu thập, quy mô và việc làm sạch bằng DGArchive. Việc loại mAGD đã biết không bảo đảm mọi miền còn lại đều thực sự lành tính.
- **DGArchive:** là dữ liệu sinh lại từ các DGA đã dịch ngược và seed đã biết. Nguồn này thích hợp làm lớp mAGD trong phép đánh giá tên miền; khác với một tập miền C2 đã được xác minh đang hoạt động trên Internet.
- **360 mẫu của dự án:** được tạo bằng script, không thu từ DNS thực, không gửi truy vấn mạng và không thực thi mã độc. Đây là dữ liệu tổng hợp có thật trong repository, nhưng chỉ thích hợp minh họa đặc trưng. Không được dùng để tuyên bố độ chính xác phát hiện FANCI hoặc botnet.

Vì vậy, câu trả lời chính xác là: **chương có phân tích kết quả trên dữ liệu thực do tác giả công bố; nhóm có chạy một minh họa tổng hợp; nhóm chưa thực hiện đánh giá FANCI trên lưu lượng mạng thực của mình.**

## Những điểm đã chỉnh để bảo đảm câu chữ chính xác

| Vị trí | Vấn đề cần làm rõ | Cách xử lý trong bản cuối |
|---|---|---|
| Đoạn phạm vi đầu chương | “Không tự huấn luyện lại” chưa nói đủ mức xác minh | Ghi rõ không có dữ liệu, mô hình và ma trận nhầm lẫn gốc; chỉ đối chiếu công bố |
| Bảng 4.1 | Có thể hiểu 1.344 ngày là độ dài lịch của khoảng ngày DGArchive | Viết “1.344 ngày có dữ liệu theo tác giả”, trong khoảng 12/2/2014–30/1/2018 |
| Mục 4.2 | Thiếu bước lấy trung bình các fold; chưa nêu đủ điều kiện của đẳng thức ACC | Nêu mức tổng hợp 5-fold và điều kiện cân bằng ngay trong tập kiểm tra đang xét |
| Mục 4.3.2 | “Sáu DGA có ACC dưới 98%” dễ bị hiểu là trung bình riêng của sáu họ | Viết các kết quả dưới ngưỡng tập trung ở sáu DGA, theo tác giả |
| Mục 4.3.4 | “Bộ đặc trưng học” sai đối tượng; kết luận về ghi nhớ quá mạnh | Viết mô hình có khả năng khái quát trong phạm vi LOGO đã xét |
| Mục 4.3.4 | SD nhỏ dễ bị hiểu là mọi họ đều có hiệu quả ổn định | Không diễn giải SD tổng hợp thành SD trực tiếp giữa 59 họ hay 1.180 lượt LOGO |
| Mục 4.6 | “Chưa biết” dùng “hoặc” không đúng nghĩa của nguồn | Đổi thành không có trong DGArchive **và cũng không** tìm thấy qua các nguồn thông dụng tại thời điểm viết bài |
| Mục 4.6 | Bản ghi mạng thực dễ bị hiểu là triển khai trực tuyến đã đo hoặc kiểm tra nghiêm ngặt theo chiều thời gian | Nêu rõ thiếu thời điểm chốt tập mAGD và phép đo độ trễ vận hành trực tuyến |
| Mục 4.6 | Ước lượng FPR dễ bị hiểu là tỷ lệ đã xác minh hoặc cận trên chắc chắn | Làm rõ thiếu thông tin về mẫu số và nhãn đầy đủ; phép chia đối chiếu là tính toán của nhóm |
| Mục 4.7 | Hai mức lưu lượng trung bình trong nguồn không nhất quán | Nêu phép tính từ 700 triệu/31 ngày, giữ số công bố theo từng ngữ cảnh |
| Mục 4.8 | Tên mục có thể khiến người đọc nghĩ cả lớp độc hại đã phân giải thành công | Làm rõ nguồn không xác nhận điều đó; đây chưa phải phép đo phát hiện C2 đã xác minh |
| Mục 4.9 | Khoảng entropy làm tròn không cho đúng số đếm 109 | Ghi số đếm sử dụng biên chưa làm tròn trong JSON |
| Mục 4.9 | Độ dài nhãn có thể bị đồng nhất với độ dài toàn tên miền FANCI | Nêu rõ khác biệt tiền xử lý; entropy không đo thứ tự ký tự |
| Mục 4.10 | “Các tập độc lập” dễ bị hiểu là không trùng mẫu | Đổi thành các tập lấy mẫu riêng; chỉ ra họ ít mẫu được dùng lại giữa các tập |

## Các bất nhất hoặc giới hạn của bài báo gốc

Đây là những điểm chưa thể giải quyết bằng cách sửa câu chữ trong báo cáo:

1. **FNR:** một số số liệu trong Bảng 5, 7, 14 và 16 không thỏa FNR = 1 − TPR, vượt mức giải thích bằng làm tròn. Chương giữ nguyên ACC/TPR/FPR đã công bố và không chép lại các cột FNR bất nhất. Không có ma trận nhầm lẫn gốc để xác định ô sai.
2. **FP thực tế:** nguồn ghi 22.345 FP tiềm năng; 22.755 − 405 = 22.350, và trừ tiếp 31 miền đã biết cũng không khớp. Vì thiếu giải thích, không dùng số này như phép tính đã kiểm chứng.
3. **Lưu lượng:** khoảng 700 triệu phản hồi trong 31 ngày cho mức trung bình khoảng 261,4 phản hồi/giây; phần hiệu năng lại nêu 164. Nguồn chưa giải thích khác biệt. Cả hai đều là số công bố theo ngữ cảnh riêng, không được tự sửa một số để khớp số kia.
4. **LOGO:** nguồn mô tả giữ lại seed/họ, nhưng chưa đặc tả đầy đủ phân bổ bNXD, mức tổng hợp và trọng số. Không tự bổ sung giả định để diễn giải SD hoặc cân bằng lớp ở mọi lượt.
5. **Chuyển mạng:** cả hai mạng dùng cùng kho mAGD. Các họ ít mẫu có thể dùng lại toàn bộ mẫu trong nhiều tập. Phép đánh giá hỗ trợ chuyển nguồn bNXD, chưa chứng minh kiểm tra trên chuỗi mAGD độc lập hoàn toàn.
6. **Theo chiều thời gian:** bản ghi kiểm tra thực tế kết thúc tháng 11/2017, còn kho DGArchive được mô tả tới tháng 1/2018. Thiếu thời điểm chốt tập huấn luyện, nên không đủ căn cứ gọi toàn bộ đánh giá là dự báo theo chiều thời gian. Điều này không tự chứng minh đã có rò rỉ dữ liệu.
7. **Miền phân giải thành công:** lớp lành tính đến từ các miền đã phân giải, nhưng lớp mAGD đến từ DGArchive; không có xác nhận mọi mAGD đã phân giải hoặc dẫn tới C2. Kết quả phân loại chuỗi chưa thay thế xác minh hạ tầng mã độc.

## Kiểm tra độc lập thực nghiệm minh họa

Đã chạy lại script với các đường dẫn đầu ra tạm riêng, rồi so sánh với kết quả lưu sẵn. CSV, JSON, hai bản bảng LaTeX và hình PNG giống từng byte. Sau đó tính lại từ CSV mà không dùng các hàm đặc trưng của script:

- 360 mẫu, 120 mẫu mỗi nhóm; các nhãn không trùng; độ dài khớp theo từng `pair_id` và phân bố độ dài giống nhau.
- Bốn đặc trưng trên từng mẫu, trung bình, SD tổng thể dùng mẫu số `n`, min/max khớp trong sai số (10^{-12}).
- Hai số đếm chồng lấn entropy là 109 và 116 khi sử dụng min/max chưa làm tròn. Dùng khoảng đã làm tròn trong bản cũ sẽ cho 105 mẫu ngẫu nhiên, nên câu chữ đã được sửa.
- Histogram chứa đủ 120 mẫu mỗi nhóm. Không có huấn luyện bộ phân loại, ngưỡng quyết định, ACC, TPR hay FPR được đo từ tập này.

SHA-256 của CSV đã kiểm tra:

```text
b3f39e0d7b5bbcb40d207c1dd4ece581f34404aa30f2462ad64136dddbd29137
```

Các phép tính bổ sung trong chương cũng đúng: 92.102/234,76 ≈ 392,3 mẫu/giây; ví dụ precision với tỷ lệ lớp giả định 0,001 cho khoảng 28,8%. Ví dụ precision là phép tính theo giả định giữ nguyên TPR/FPR, không phải số đo trên mạng thực.

## Khuyến nghị sử dụng bản cuối

### Chuẩn hóa văn phong theo Chương 1–3

Sau khi đối chiếu trực tiếp ba chương đầu, Chương 4 đã được chỉnh theo cách trình bày cơ chế, kết quả và ý nghĩa của báo cáo. Phần mở đầu nêu nội dung bằng câu trần thuật; các câu hướng dẫn như “cần dùng” hoặc “không được dùng” được chuyển thành nhận xét có điều kiện. Các chi tiết khoa học về nhãn, LOGO, dữ liệu lịch sử và FPR vẫn được giữ.

Thuật ngữ được thống nhất: “máy chủ phân giải DNS”, “bộ phân loại được huấn luyện”, “tên miền”, “hậu tố công khai”, “độ chính xác (ACC)”, “tỷ lệ dương tính giả (FPR)”, “khả năng tổng quát hoá” và “module tình báo”. “Module”, “kernel” và “seed” được giữ theo cách dùng đã giới thiệu ở các chương trước; “script”, “repository” và “recall” trong văn xuôi được thay bằng “chương trình Python”, “kho mã nguồn” và “TPR”. Precision được giới thiệu là “độ chuẩn xác” để phân biệt với ACC.

Các bảng số liệu, phương trình, nhãn tham chiếu và khóa trích dẫn không đổi trong đợt biên tập văn phong. Chương 1–3 được dùng làm mẫu đối chiếu, không được sửa trong đợt này.

Có thể dùng nội dung này cho tiểu luận và thuyết trình, với cách giới thiệu: “Nhóm phân tích kết quả công bố của FANCI và thực hiện minh họa đặc trưng trên dữ liệu tổng hợp.” Không giới thiệu là đã tái lập toàn bộ FANCI, đã xác minh 10 DGA mới hoặc đã đo độ chính xác trên mạng thực của nhóm.

Giới hạn của cả báo cáo cần xử lý riêng khi chuẩn bị nộp: README đặt mục tiêu 15–30 trang, còn bản chương 4 chi tiết chiếm hơn mức dự kiến 5–6 trang cho chương này. Đợt rà soát hiện tại giữ độ chi tiết theo yêu cầu, không tự rút gọn nội dung các chương khác.
