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


if __name__ == "__main__":
    unittest.main()
