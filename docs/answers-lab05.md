# Câu hỏi thảo luận - Lab 05: Hotfix flow & bảo trì nhiều phiên bản

## 1. Vì sao ở Phần A chưa gắn tag `v1.1.0`? Nếu đã gắn rồi thì bây giờ phải phát hành `v1.1.1`? (Slide 60)
- **Tính bất biến của Tag trong SCM:** Trong Git và chuẩn Semantic Versioning, annotated tag đại diện cho một mốc phát hành chính thức (`immutable baseline`). Một khi tag đã được tạo và push ra remote chia sẻ với người dùng/hệ thống, quy tắc cốt lõi là: *"Tag đã chia sẻ thì không xóa, không di chuyển"*.
- **Trạng thái của nhánh release trước khi phát hành:** Ở Phần A, nhánh `release/lab05` mới chỉ đóng vai trò là một bản ứng viên phát hành (Release Candidate) được rẽ từ `master` để chuẩn bị nộp bài và kiểm thử giai đoạn cuối, chưa phải bản release cuối cùng.
- **Tác động nếu gắn tag quá sớm:** Nếu đã gắn tag `v1.1.0` ngay ở Phần A, thì khi phát hiện lỗi ở Phần B và tiến hành sửa lỗi ở Phần C & E, các commit sửa lỗi đưa vào `release/lab05` sẽ làm thay đổi mã nguồn so với tag `v1.1.0`. Theo đúng đặc tả SemVer, khi mã nguồn thay đổi sau khi đã đóng dấu phát hành, ta không được ghi đè tag cũ mà bắt buộc phải phát hành bản vá mới với phiên bản tăng lên là `v1.1.1`.
- **Kết luận:** Giữ nhánh `release/lab05` chưa gắn tag cho phép đội ngũ phát triển tích hợp nốt bản vá hotfix của tuần hiện tại vào nhánh release trước khi chính thức chốt baseline bằng tag `v1.1.0`.

---

## 2. Ưu và nhược điểm của Upstream First so với Release First? (Slide 64)

### Mô hình Upstream First (Sửa trên `master` trước $\rightarrow$ cherry-pick về `release/*`):
- **Ưu điểm:**
  - Nhánh chính (`master`) luôn được cập nhật bản vá ngay lập tức, ngăn ngừa hoàn toàn nguy cơ tái phát sinh lỗi (regression) ở các phiên bản phát hành trong tương lai.
  - Phù hợp với các dự án phần mềm quy mô lớn, phát triển liên tục theo chu kỳ sprint (điển hình như mô hình Microsoft Release Flow).
- **Nhược điểm:**
  - Nhánh `master` có thể đã phát triển thêm nhiều tính năng mới hoặc thay đổi kiến trúc so với phiên bản release đang chạy trên production. Do đó, việc cherry-pick bản vá từ `master` ngược về `release/*` cũ có thể gặp xung đột mã nguồn nghiêm trọng hoặc kéo theo những phụ thuộc không tương thích.

### Mô hình Release First (Sửa trên `release/*` trước $\rightarrow$ cherry-pick/merge về `master`):
- **Ưu điểm:**
  - Bản sửa lỗi được viết, kiểm thử và xác minh trực tiếp trên chính môi trường/baseline đang gặp sự cố của khách hàng trên production, giảm thiểu tối đa rủi ro gây lỗi phụ.
  - Cho phép xuất bản bản vá khẩn cấp (Emergency Hotfix Patch `v1.0.1`) cho người dùng ngay lập tức mà không cần chờ đợi hay phụ thuộc vào tiến độ tính năng trên `master`.
  - Rất phù hợp với bối cảnh học phần IT3180 (nộp bài theo tuần và bảo trì song song nhiều phiên bản).
- **Nhược điểm:**
  - Đòi hỏi quy trình kỷ luật nghiêm ngặt: sau khi sửa trên release, bắt buộc lập trình viên phải nhớ lan truyền (cherry-pick `-x`) về `master` và các nhánh release đang hoạt động khác; nếu bỏ quên, lỗi sẽ tồn tại âm thầm trong các phiên bản tiếp theo.

---

## 3. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện? (Slide 64)
- **Lệnh kiểm tra hành vi tự động bằng vòng lặp trên cả 3 dòng phiên bản (Slide 61):**
  ```bash
  for ref in v1.0.1 v1.1.0 master; do
      git switch --detach -q $ref; printf "%-8s " $ref
      python -c "from aims.dvd import DigitalVideoDisc as D; from aims.search import search_by_title; \
      print(len(search_by_title([D('The Lion King')], 'lion')))"
  done; git switch -q master
  ```
  Nếu quên lan truyền bản sửa sang `release/lab05`, nhánh này (và tag `v1.1.0` được tạo từ nó) sẽ vẫn giữ nguyên mã nguồn cũ (phân biệt hoa thường). Khi vòng lặp chạy, kết quả in ra sẽ là:
  ```text
  v1.0.1   1
  v1.1.0   0
  master   1
  ```
  Số `0` tại dòng `v1.1.0` sẽ ngay lập tức phát hiện ra việc thiếu sót bản sửa lỗi.
- **Lệnh kiểm toán commit cherry-pick trong lịch sử:**
  ```bash
  git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"
  ```
  Nếu quên lan truyền sang `release/lab05`, lệnh này sẽ chỉ trả về **1 commit duy nhất** (trên `master`) thay vì đủ **2 commit** (trên cả `master` và `release/lab05`).
