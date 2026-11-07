# Câu hỏi thảo luận - Lab 04: Release flow & phiên bản phát hành

## 1. Vì sao chuẩn bị trên `master` trước, không sửa trên nhánh `release`? (Slide 47)
- **Tuân thủ nguyên tắc Single Source of Truth:** Trong mô hình Release Flow, nhánh `master` luôn là nguồn sự thật duy nhất phản ánh trạng thái mã nguồn mới nhất sẵn sàng phát hành. Việc chuẩn bị phát hành (như cập nhật phiên bản `__version__ = "1.0.0"`, cập nhật lời chào ứng dụng, tổng hợp tài liệu `CHANGELOG.md` và kiểm thử tích hợp) cần được hoàn thành và kiểm tra kỹ lưỡng trên `master` trước khi rẽ nhánh phát hành.
- **Mục đích của nhánh release:** Nhánh `release/labXX` được tạo ra nhằm mục đích "đóng băng" (stabilize/freeze baseline) cấu hình tại thời điểm phát hành/nộp bài. Nó đóng vai trò là dòng bảo trì ổn định, không phải là nơi để tiếp tục thực hiện các thay đổi mã nguồn hay chuẩn bị tính năng.
- **Tránh merge ngược:** Nếu sửa trực tiếp trên nhánh `release`, sau đó bắt buộc phải merge ngược về `master` để đồng bộ. Điều này vi phạm nguyên tắc cốt lõi của Release Flow: *"release/\* không bao giờ merge ngược vào master"*, đồng thời dễ gây ra xung đột (conflict) hoặc phân kỳ lịch sử (divergence) ngoài ý muốn.

---

## 2. Vì sao `release/*` không bao giờ merge ngược vào `master`? So sánh với GitFlow (Slide 52)
- **Trong Release Flow:**
  - Quy tắc bất biến số 4 của Release Flow quy định: `release/* không bao giờ merge ngược vào master`.
  - Mọi công việc chuẩn bị cho bản phát hành đều đã được hoàn thiện trên `master` trước khi tạo nhánh release. Do đó, nhánh release là bản chụp (snapshot) đóng băng của `master` tại thời điểm đó.
  - Khi có lỗi phát sinh sau phát hành trên production, bản vá (hotfix) sẽ được tạo riêng và áp dụng cho nhánh release cần vá, sau đó được cherry-pick hoặc đưa qua PR riêng về `master` theo quy trình có kiểm soát, chứ không bao giờ merge ngược toàn bộ nhánh release vào `master`. Điều này đảm bảo không làm ô nhiễm `master` với các commit đóng băng hoặc ghi đè những tính năng mới hơn đang phát triển trên `master`.
- **So sánh với GitFlow:**
  - Trong **GitFlow**, có 2 nhánh sống dài hạn là `master` (hoặc `main`) và `develop`. Nhánh `release` được tách từ `develop` để kiểm thử giai đoạn cuối. Khi release sẵn sàng, GitFlow thực hiện **dual-merge**: merge nhánh `release` vào `master` (để phát hành) và merge ngược lại vào `develop` (để đồng bộ các bản vá trong quá trình đóng băng).
  - GitFlow có độ phức tạp cao hơn nhiều, đòi hỏi quản lý đồng thời hai nhánh dài hạn, dễ xảy ra merge hell và xung đột khi merge ngược vào `develop`. Ngược lại, **Release Flow** (chuẩn của Microsoft và các tổ chức CI/CD hiện đại) tinh gọn hơn: chỉ có duy nhất `master` làm nhánh tích hợp liên tục, các nhánh `release/*` chỉ rẽ nhánh độc lập khi phát hành và tuyệt đối không merge ngược vào `master`.

---

## 3. Vì sao lên `1.0.0` mà không phải `0.4.0`? (Slide 52)
- **Quy chuẩn Semantic Versioning (SemVer 2.0.0 - `MAJOR.MINOR.PATCH`):**
  - Các phiên bản dạng `0.y.z` đại diện cho giai đoạn phát triển sơ khai (initial development). Ở giai đoạn này, API và cấu trúc mã nguồn chưa ổn định, có thể thay đổi liên tục mà không cần tuân thủ nghiêm ngặt tính tương thích ngược. Các bài thực hành Lab 01, 02, 03 được đánh số lần lượt là `v0.1.0`, `v0.2.0`, `v0.3.0`.
  - Phiên bản `1.0.0` là dấu mốc quan trọng công bố phiên bản phát hành chính thức đầu tiên (First Stable / Production Release). Khi nâng lên `1.0.0`, sản phẩm đã xác lập một **Public API / Baseline ổn định**, có hợp đồng rõ ràng và cam kết tính tương thích ngược (backward compatibility) cho các bản cập nhật tiếp theo trong dòng `1.x`.
- **Thực tế dự án AIMS-mini tại Lab 04:**
  - Dự án đã hoàn thiện đầy đủ các chức năng cốt lõi: mô hình thực thể DVD (`DigitalVideoDisc`), giỏ hàng (`Cart`), in biên lai (`print_cart`), tìm kiếm theo tiêu đề (`search_by_title`), tính toán chiết khấu (`total_cost_with_discount`), tài liệu Use Case, kiểm thử tự động toàn diện (`tests/`), và tài liệu thay đổi chuẩn mực (`CHANGELOG.md`).
  - Dự án đã hoàn thiện trọn vẹn quy trình SCM: kiểm soát thay đổi qua PR & Review, Branch Protection, đóng băng cấu hình (Baseline & Tag) và xuất bản chính thức trên GitHub Release. Vì vậy, việc nâng phiên bản lên `1.0.0` là hoàn toàn chính xác theo nguyên tắc SemVer và thực tế phát triển phần mềm.
