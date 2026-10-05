# Minh họa đặc trưng chuỗi tên miền cho Chương 4

Thư mục này chứa một thực nghiệm **đã chạy**, có thể tái tạo, nhằm minh họa bốn đặc trưng chuỗi tên miền. Đây là mô phỏng giáo dục, không phải bản cài đặt đầy đủ FANCI, không phải đánh giá trên lưu lượng NXDomain thực tế và không phải tái lập các chỉ số ACC/TPR/FPR của bài báo.

## Chạy lại

```powershell
python Experiments/feature_demo.py
```

CSV, JSON và bảng LaTeX chỉ dùng thư viện chuẩn Python. Tạo hình PNG cần `Pillow` (đã có trong runtime đi kèm Codex). Để chỉ sinh số liệu:

```powershell
python Experiments/feature_demo.py --no-figure
```

Lệnh đã chạy trong môi trường hiện tại:

```powershell
& 'C:\Users\admin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' Experiments/feature_demo.py
```

Môi trường được kiểm chứng: Python 3.12.14. Mã tự tìm thư mục gốc từ vị trí script, nên đầu ra mặc định không phụ thuộc thư mục làm việc khi gọi script bằng đường dẫn đúng. Cũng có thể chỉ định `--output-dir`, `--figure` và `--table`.

## Đầu vào: 360 mẫu tổng hợp

Mỗi nhóm có 120 mẫu. Mọi tên miền đều có dạng `<nhãn>.invalid`; script **không gửi truy vấn DNS**, không truy cập mạng, không chạy mã độc. Không gán nhãn xác nhận lành tính/độc hại cho bất kỳ tên miền thật nào.

1. **Đối chứng dễ đọc (`readable_control`)**: lấy toàn bộ 12 × 10 tổ hợp có thứ tự giữa `PREFIXES` và `SUFFIXES` được ghi trực tiếp trong mã. Các tiền tố liên quan tới học tập, ví dụ `campus`, `student`, `research`; hậu tố là chức năng thông thường, ví dụ `portal`, `login`, `notes`. Những tổ hợp này chỉ đại diện cho nhãn có chủ ý của người đặt tên; không được coi là bNXD thu thập từ mạng.
2. **Mô phỏng ngẫu nhiên (`uniform_letters`)**: dùng bộ sinh giả ngẫu nhiên `random.Random(2018)` để chọn độc lập mỗi chữ cái theo phân bố đều trên `a`–`z`. Mỗi nhãn được sinh đúng bằng độ dài nhãn đối chứng cùng `pair_id`; nếu trùng trong nhóm thì sinh lại. Đây chỉ mô phỏng biểu hiện chuỗi giống ngẫu nhiên của một số DGA kiểu tính toán, không triển khai thuật toán của một họ mã độc cụ thể.
3. **Mô phỏng ghép từ (`wordlist_pairs`)**: lập mọi tổ hợp có thứ tự của hai từ trong danh sách 72 từ `WORDS` được ghi trực tiếp trong mã; ghép không có dấu phân cách; loại các chuỗi trùng; phân nhóm theo độ dài; sắp xếp rồi xáo trộn; lấy không hoàn lại trong từng nhóm độ dài. Mỗi nhãn có độ dài khớp đối chứng cùng `pair_id`. Mục đích là cho thấy chuỗi được sinh tự động từ các từ tự nhiên vẫn có thể giống chuỗi dễ đọc về mặt đặc trưng.

Thứ tự sinh được cố định: khởi tạo RNG với seed 2018; xáo trộn 120 đối chứng; xáo trộn các nhóm cặp từ theo thứ tự độ dài tăng; với mỗi đối chứng, sinh nhãn ngẫu nhiên rồi lấy một cặp từ bằng `pop()` của nhóm đúng độ dài. Số liệu lưu sẵn trong CSV là đầu vào tham chiếu nếu dùng phiên bản Python khác.

Cả ba nhóm có **đúng cùng phân bố độ dài**: 9 ký tự: 2 mẫu; 10: 12; 11: 34; 12: 50; 13: 20; 14: 2. Cả ba cùng chỉ sử dụng chữ cái `a`–`z`, có một nhãn trước hậu tố. Thiết kế này hạn chế việc tạo ra sự khác nhau đơn thuần do độ dài hoặc do thêm chữ số vào riêng một nhóm; vẫn còn thiên lệch do vốn từ và cơ chế sinh mẫu.

## Bốn đặc trưng và quy ước

Tiền xử lý: chuyển chữ thường, bỏ đúng hậu tố `.invalid`, phân tích phần nhãn còn lại. Không dùng Public Suffix List, IDNA, xử lý subdomain hay các nhánh tiền xử lý khác của FANCI.

Với nhãn `s`, độ dài `L`, số lần xuất hiện ký tự `c` là `n_c` và tập ký tự phân biệt `A`:

- `length`: `L = len(s)`. Đây là độ dài **nhãn đã bỏ hậu tố**, không phải độ dài toàn tên miền như đặc trưng cấu trúc số 1 trong Chương 3.
- `vowel_ratio`: tổng số lần xuất hiện `a`, `e`, `i`, `o`, `u` chia cho `L`; không coi `y` là nguyên âm.
- `entropy_bits`: `H = -sum((n_c / L) * log2(n_c / L) for c in A)`. Tổng chạy trên **các ký tự phân biệt**, mỗi ký tự đúng một lần. Đây là entropy Shannon của phân bố ký tự thực nghiệm, không phải entropy rate của nguồn sinh và không đo thứ tự ký tự.
- `repeated_char_ratio`: số ký tự phân biệt xuất hiện ít nhất hai lần chia cho `len(A)`. Đây không phải tỷ lệ các vị trí bị lặp và không phải `1 - len(A)/L`.

Các đặc trưng trên có liên quan tới ý tưởng của FANCI nhưng chỉ là **phiên bản rút gọn** trên các fixture một nhãn. Không được coi đây là trích xuất đầy đủ 21 đặc trưng FANCI.

## Kết quả đã chạy

Các giá trị dưới đây là trung bình ± độ lệch chuẩn tổng thể của 120 mẫu trong mỗi nhóm. SD dùng mẫu số `n`, không phải `n - 1`; đây là thống kê mô tả của toàn bộ tập minh họa, không phải khoảng tin cậy cho một quần thể lưu lượng DNS.

| Nhóm | Độ dài nhãn | Tỷ lệ nguyên âm | Entropy (bit) | Tỷ lệ ký tự phân biệt lặp |
|---|---:|---:|---:|---:|
| Đối chứng dễ đọc | 11.67 ± 0.98 | 0.380 ± 0.064 | 3.080 ± 0.206 | 0.260 ± 0.147 |
| Mô phỏng ngẫu nhiên | 11.67 ± 0.98 | 0.177 ± 0.107 | 3.140 ± 0.252 | 0.211 ± 0.130 |
| Mô phỏng ghép từ | 11.67 ± 0.98 | 0.359 ± 0.061 | 3.038 ± 0.237 | 0.301 ± 0.154 |

Tỷ lệ nguyên âm trung bình của nhóm chữ ngẫu nhiên thấp hơn hai nhóm có từ tự nhiên. Entropy trung bình chỉ khác nhau ít, và các miền giá trị chồng lấn nhiều: 109/120 mẫu ngẫu nhiên cùng 116/120 mẫu ghép từ nằm trong khoảng entropy của đối chứng, xấp xỉ `[2.5566567, 3.4594316]`. Số đếm dùng min/max **chưa làm tròn** trong JSON (`2.556656707462823` và `3.4594316186372973`); không dùng hai biên đã làm tròn ở câu trước. Đây là đếm mẫu nằm trong một khoảng mô tả, **không phải số lỗi phân loại**. Sự chồng lấn cho thấy không thể dùng kết quả này để kết luận một ngưỡng entropy riêng lẻ sẽ phân loại hiệu quả; ghép từ vẫn giữ nhiều đặc điểm giống đối chứng.

Không có bước huấn luyện, chọn ngưỡng, dự đoán, confusion matrix, ACC, TPR hay FPR trong thực nghiệm này. Không thể suy từ các trung bình trên thành hiệu quả phát hiện botnet thực tế. Cần dữ liệu có nhãn thực, giao thức đánh giá đúng, toàn bộ pipeline và bộ phân loại để đánh giá FANCI.

## Tệp đầu ra

- `results/samples_features.csv`: 360 hàng mẫu, gồm `group`, `pair_id`, `domain`, `normalized_label` và bốn đặc trưng; mỗi `pair_id` liên kết ba nhãn cùng độ dài.
- `results/summary.json`: seed, nguồn mô phỏng, số mẫu, phân bố độ dài, trung bình, độ lệch chuẩn tổng thể, min/max, số mẫu chồng lấn khoảng entropy, phiên bản Python và hạn chế.
- `results/summary_table.tex`: thân bảng `tabularx` tương thích với template báo cáo; đầu bảng quy định 120 mẫu/nhóm; các ô dùng trung bình ± SD.
- `../Template/Figures/Bang4_MinhHoaDacTrung.tex`: bản bảng dùng trực tiếp trong báo cáo, giống hệt `results/summary_table.tex`. Bảng và hình cùng nằm trong `Template` để có thể upload nguyên thư mục `Template` lên Overleaf; không cần đưa thư mục `Experiments` vào để biên dịch báo cáo.
- `../Template/Figures/Chuong4_MinhHoaDacTrung.png`: hình 2400 × 1400 pixel, 300 DPI, nhãn tiếng Việt và cỡ chữ được tăng cho bản báo cáo rộng 16 cm. Panel (a) là scatter tỷ lệ nguyên âm/entropy, có ký hiệu khác nhau cho từng nhóm; các điểm trùng đặc trưng có thể đè lên nhau. Panel (b) là histogram entropy với bin rộng 0.2 bit, hiển thị số mẫu bằng cột ghép theo nhóm; mỗi nhóm có tổng 120 mẫu.

SHA-256 của CSV sau lần chạy đã kiểm chứng:

```text
b3f39e0d7b5bbcb40d207c1dd4ece581f34404aa30f2462ad64136dddbd29137
```

Để kiểm tra lại trên PowerShell: `Get-FileHash Experiments/results/samples_features.csv -Algorithm SHA256`. Hình dùng Arial trên Windows, hoặc DejaVu Sans trên Linux; thay đổi font có thể thay đổi pixel của hình, không thay đổi CSV và thống kê. JSON ghi phiên bản Python nên có thể khác trường phiên bản khi chuyển môi trường.
