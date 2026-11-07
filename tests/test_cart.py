import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            res = cart.add_dvd(DigitalVideoDisc(f"DVD {i}", cost=10.0))
            self.assertTrue(res)
        # Đĩa thứ 21 phải trả về False
        res_21 = cart.add_dvd(DigitalVideoDisc("DVD 21", cost=10.0))
        self.assertFalse(res_21)

    def test_discount_calculation(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD 1", cost=100.0))
        discounted = cart.total_cost_with_discount(20)
        self.assertAlmostEqual(discounted, 80.0)

    def test_discount_invalid_percent(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD 1", cost=100.0))
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(-10)

    def test_sort_by_title(self):
        cart = Cart()
        dvd_b = DigitalVideoDisc("The Lion King", cost=19.95)
        dvd_a = DigitalVideoDisc("Aladdin", cost=18.99)
        dvd_c = DigitalVideoDisc("Star Wars", cost=24.95)
        cart.add_dvd(dvd_b)
        cart.add_dvd(dvd_a)
        cart.add_dvd(dvd_c)
        cart.sort_by_title()
        self.assertEqual([d.title for d in cart.items], ["Aladdin", "Star Wars", "The Lion King"])

    def test_sort_by_cost(self):
        cart = Cart()
        dvd1 = DigitalVideoDisc("DVD 1", cost=25.0)
        dvd2 = DigitalVideoDisc("DVD 2", cost=10.0)
        dvd3 = DigitalVideoDisc("DVD 3", cost=15.0)
        cart.add_dvd(dvd1)
        cart.add_dvd(dvd2)
        cart.add_dvd(dvd3)
        cart.sort_by_cost()
        self.assertEqual([d.cost for d in cart.items], [10.0, 15.0, 25.0])
        cart.sort_by_cost(reverse=True)
        self.assertEqual([d.cost for d in cart.items], [25.0, 15.0, 10.0])


if __name__ == "__main__":
    unittest.main()
