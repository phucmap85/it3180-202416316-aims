# AIMS-mini Use Case Diagram & Specification

## 1. Giới thiệu
Tài liệu mô tả các trường hợp sử dụng (Use Cases) của hệ thống AIMS-mini.

## 2. Danh sách Use Cases
- **UC01: Thêm DVD vào giỏ hàng (Add DVD to Cart)**
  - Actor: Khách hàng (Customer)
  - Mô tả: Khách hàng chọn DVD và thêm vào giỏ hàng (tối đa 20 đĩa).
- **UC02: Xóa DVD khỏi giỏ hàng (Remove DVD from Cart)**
  - Actor: Khách hàng
  - Mô tả: Khách hàng xóa một DVD đã có ra khỏi giỏ hàng.
- **UC03: Xem chi tiết giỏ hàng (Print Cart)**
  - Actor: Khách hàng
  - Mô tả: In danh sách các DVD trong giỏ hàng kèm tổng tiền thanh toán.
- **UC04: Tìm kiếm DVD theo tiêu đề (Search by Title)**
  - Actor: Khách hàng
  - Mô tả: Tìm kiếm các đĩa DVD có chứa từ khóa chỉ định trong tiêu đề.

## 3. Sơ đồ Use Case
```text
+-------------------------------------------------------+
|                       AIMS-mini                       |
|                                                       |
|   (User) ----> [UC01: Add DVD to Cart]                |
|          ----> [UC02: Remove DVD from Cart]           |
|          ----> [UC03: Print Cart Details]             |
|          ----> [UC04: Search DVD by Title]            |
|                                                       |
+-------------------------------------------------------+
```
