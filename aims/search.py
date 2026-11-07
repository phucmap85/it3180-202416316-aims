def search_by_category(items, category):
    """Tìm kiếm DVD theo thể loại."""
    return [dvd for dvd in items if category.lower() in dvd.category.lower()]


def search_by_title(items, keyword):
    """Tìm kiếm DVD theo tiêu đề."""
    return [dvd for dvd in items if keyword in dvd.title]
