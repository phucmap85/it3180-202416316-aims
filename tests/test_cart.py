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


if __name__ == "__main__":
    unittest.main()
