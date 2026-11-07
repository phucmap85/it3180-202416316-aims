# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-11-07

### Added
- `Cart.sort_by_title()`: Sắp xếp các DVD trong giỏ hàng theo tiêu đề (alphabet).
- `Cart.sort_by_cost()`: Sắp xếp các DVD trong giỏ hàng theo giá tiền.
- `search_by_category()`: Tìm kiếm đĩa DVD theo thể loại trong `aims.search`.

## [1.0.1] - 2026-11-07

### Fixed
- Tìm kiếm theo tiêu đề không phân biệt chữ hoa, chữ thường (Refs #18).

## [1.0.0] - 2026-11-07

### Added
- `Cart.print_cart()`: Hiển thị chi tiết danh sách đĩa DVD và tổng giá trị trong giỏ hàng.
- `search_by_title()`: Tìm kiếm đĩa DVD theo từ khóa tiêu đề trong `aims.search`.
- `Cart.total_cost_with_discount()`: Tính tổng chi phí giỏ hàng sau khi áp dụng phần trăm giảm giá.
- Tài liệu mô tả và sơ đồ Use Case tại `docs/use-case.md`.
- Bộ kiểm thử tự động (Unit Tests) trong thư mục `tests/`.

### Fixed
- Sửa lỗi logic giới hạn giỏ hàng cho phép nhận đĩa thứ 21 khi tối đa chỉ được 20 đĩa (#7).
- Bổ sung xác thực kiểm tra tính hợp lệ của phần trăm giảm giá (0 <= percent <= 100).
