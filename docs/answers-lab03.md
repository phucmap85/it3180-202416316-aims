# Báo cáo thảo luận Lab 03: Bugfix flow, xung đột & hoàn tác

## Câu hỏi 1: Merge base là gì?

1. **Định nghĩa kỹ thuật**:
   - `Merge base` giữa hai nhánh (hoặc giữa hai commit $A$ và $B$) là **tổ tiên chung gần nhất (Lowest Common Ancestor - LCA)** của hai nhánh đó trong đồ thị lịch sử commit (Directed Acyclic Graph - DAG).
   - Git xác định điểm này thông qua lệnh ngầm `git merge-base A B`.

2. **Vai trò trong quá trình 3-way merge**:
   - Khi thực hiện hòa nhập 2 nhánh, Git sử dụng thuật toán 3-way merge dựa trên 3 phiên bản:
     - Phiên bản gốc chung: `Merge base` (tổ tiên chung).
     - Phiên bản hiện tại của nhánh đích: `HEAD` (ours).
     - Phiên bản của nhánh cần merge: `Branch` (theirs).
   - Git so sánh sự khác biệt của `HEAD` so với `Merge base` và của `Branch` so với `Merge base`:
     - Nếu một dòng chỉ bị sửa đổi ở một nhánh so với `Merge base`, Git sẽ tự động chấp nhận thay đổi đó.
     - Nếu cả hai nhánh cùng sửa đổi cùng một dòng (hoặc một bên sửa một bên xóa) so với `Merge base`, Git sẽ không thể tự quyết định và thông báo `CONFLICT` (xung đột) yêu cầu người dùng giải quyết thủ công.

---

## Câu hỏi 2: Vì sao `master` và `release/*` phải dùng `revert` thay vì `reset`?

1. **Bảo toàn tính bất biến của lịch sử dùng chung (Immutability of Shared History)**:
   - Các nhánh `master` và `release/*` là các nhánh công khai, được chia sẻ với toàn bộ thành viên trong nhóm phát triển và hệ thống CI/CD/Production.
   - Lệnh `git reset` (nhất là `git reset --hard`) hoạt động bằng cách **viết lại lịch sử** (xóa bỏ commit và lùi con trỏ nhánh). Nếu một commit đã được các thành viên khác pull về máy, việc dùng `reset` và force push lên remote sẽ khiến lịch sử giữa remote và local của các thành viên bị phân tách (diverge), gây ra lỗi nghiêm trọng và xung đột lớn khi họ tiếp tục push/pull.

2. **Cơ chế an toàn của `git revert`**:
   - Thay vì xóa bỏ commit cũ, `git revert` tạo ra một **commit mới hoàn toàn** có nội dung đảo ngược lại các thay đổi của commit cần hủy bỏ.
   - Lịch sử Git luôn đi thẳng về phía trước (append-only), minh bạch, dễ kiểm toán (audit trail) và truy vết nguồn gốc.
   - Mọi thành viên chỉ cần `git pull` bình thường là nhận được bản hoàn tác mà không bị hỏng nhánh hay mất code. Vì vậy, trên các nhánh công khai và nhánh release bắt buộc phải dùng `git revert` (thông qua Pull Request).
