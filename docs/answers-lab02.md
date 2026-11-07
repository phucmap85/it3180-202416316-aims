# Báo cáo thảo luận Lab 02: Feature/Topic Flow & Pull Request

## Câu hỏi 1: Vì sao phải đồng bộ master trước khi gửi Pull Request (PR)?

1. **Phát hiện và giải quyết xung đột sớm (Early Conflict Resolution)**:
   - Trong môi trường phát triển nhóm, trong khi lập trình viên đang làm việc trên nhánh tính năng, nhánh `master` có thể đã được cập nhật bởi các Pull Request khác từ đồng nghiệp (ví dụ thực tế trong bài lab: Dev 2 đang phát triển `feature/search-by-title` từ master cũ thì Dev 1 đã merge `feature/cart-print` vào master).
   - Nếu không đồng bộ `master` về nhánh của mình trước, lập trình viên sẽ không biết code của mình có xung đột với code mới nhất hay không. Khi mở PR, GitHub có thể báo xung đột và ngăn cản việc merge tự động. Việc đồng bộ giúp giải quyết xung đột ngay trên máy cá nhân một cách chủ động.

2. **Kiểm thử tích hợp trước khi đưa lên nhánh chính (Principle of Verification)**:
   - Tuân thủ nguyên tắc SCM cốt lõi: *"Thứ được duyệt = Thứ được tích hợp"*.
   - Sau khi merge `origin/master` vào nhánh tính năng, lập trình viên có thể chạy kiểm thử toàn diện (ví dụ chạy `python main.py` kiểm tra kết quả `Total cost: 63.89 $`) để đảm bảo các thay đổi mới kết hợp cùng mã nguồn hiện tại của hệ thống không gây ra lỗi hồi quy (regression bugs) trước khi gửi PR cho người khác đánh giá.

3. **Giữ Pull Request gọn gàng và tập trung**:
   - Tab "Files changed" của PR sẽ chỉ thể hiện đúng các thay đổi thực sự của tính năng cần review so với trạng thái mới nhất của `master`, giúp người review dễ dàng kiểm tra và phê duyệt.

---

## Câu hỏi 2: Khi nào không được rebase?

1. **Quy tắc vàng của Rebase (The Golden Rule of Rebase)**:
   - **Tuyệt đối không bao giờ rebase các commit đã được chia sẻ công khai lên remote repository** hoặc nằm trên các nhánh dùng chung / nhánh bảo vệ (chẳng hạn như `master`, `main`, `release/*`).

2. **Nguyên nhân kỹ thuật**:
   - Lệnh `rebase` hoạt động bằng cách tạo ra các commit hoàn toàn mới với mã băm (SHA hash) mới và viết lại lịch sử commit.
   - Nếu một commit đã được đồng nghiệp kéo (pull) về máy cục bộ của họ mà ta lại rebase và push đè (force push) lên remote, lịch sử của remote và local của đồng nghiệp sẽ bị phân tách (diverge). Khi đồng nghiệp đồng bộ lại, Git sẽ cố gắng merge 2 luồng lịch sử song song này, dẫn đến hàng loạt commit trùng lặp và xung đột merge nghiêm trọng ("merge hell").

3. **Khi nào ĐƯỢC PHÉP rebase**:
   - Chỉ nên dùng rebase trên nhánh cục bộ (local branch) hoặc nhánh tính năng cá nhân chưa được push/chia sẻ cho người khác, nhằm mục đích gộp commit hoặc làm sạch lịch sử trước khi tích hợp vào nhánh chính.

---

## Câu hỏi 3: Nhánh `feature/*` khác `topic/*` ra sao?

| Tiêu chí | Nhánh `feature/*` | Nhánh `topic/*` |
| :--- | :--- | :--- |
| **Mục đích** | Phát triển một tính năng nghiệp vụ cụ thể của sản phẩm cho người dùng cuối. | Thực hiện một chủ đề công việc phụ trợ, thử nghiệm kỹ thuật, tài liệu hoặc cấu hình. |
| **Ví dụ thực tế trong bài lab** | `feature/cart-print`, `feature/search-by-title` | `topic/pr-template`, `topic/use-case-diagram` |
| **Vòng đời & Phạm vi** | Vòng đời theo chu kỳ phát triển tính năng, thường liên quan đến logic mã nguồn (source code) và test. | Vòng đời cực kỳ ngắn, thường chỉ tập trung vào một tác vụ đơn lẻ (tài liệu, cấu hình build, CI template). |
| **Mức độ ảnh hưởng** | Thay đổi trực tiếp hành vi hoạt động của phần mềm (thêm hàm, thêm class, nghiệp vụ). | Thường không làm thay đổi trực tiếp logic nghiệp vụ sản phẩm (như bổ sung docs, template PR). |
