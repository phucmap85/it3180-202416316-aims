import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):
    def test_search_by_title(self):
        d1 = DigitalVideoDisc("The Lion King", cost=19.95)
        d2 = DigitalVideoDisc("Star Wars", cost=24.95)
        results = search_by_title([d1, d2], "Lion")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "The Lion King")

    def test_search_by_title_case_insensitive(self):
        d1 = DigitalVideoDisc("The Lion King", cost=19.95)
        d2 = DigitalVideoDisc("Star Wars", cost=24.95)
        results = search_by_title([d1, d2], "lion")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "The Lion King")


if __name__ == "__main__":
    unittest.main()
