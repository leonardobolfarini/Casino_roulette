from unittest import TestCase
from roleta import Bet, Roulette


class RoletaTest(TestCase):

    def test_run_test(self):
        self.assertTrue(True)


    def test_black(self):
        bet = Bet.create_black(value=100.)
        self.assertIsInstance(bet, Bet)
        self.assertEqual(bet.value, 100.)
        black = {
            2, 4, 6, 8, 10, 11, 13, 15,
            17, 20, 22, 24, 26, 28, 29, 31, 33, 35
        }
        self.assertSetEqual(bet.numbers, black)

    def test_red(self):
        bet = Bet.create_red(value=100.)
        self.assertIsInstance(bet, Bet)
        self.assertEqual(bet.value, 100.)
        red = {
            1, 3, 5, 7, 9, 12,
            14, 16, 18, 19,
            21, 23, 25, 27,
            30, 32, 34, 36
        }
        self.assertSetEqual(bet.numbers, red)

    def test_odd(self):
        bet = Bet.create_odd(value=100.)
        self.assertIsInstance(bet, Bet)
        self.assertEqual(bet.value, 100.)
        self.assertEqual(len(bet.numbers), 18)
        self.assertEqual(len(list(filter(lambda it: it % 2 == 0, bet.numbers))), 0)

    def test_even(self):
        bet = Bet.create_even(value=100.)
        self.assertIsInstance(bet, Bet)
        self.assertEqual(bet.value, 100.)
        self.assertEqual(len(bet.numbers), 18)
        self.assertEqual(len(list(filter(lambda it: it % 2 == 1, bet.numbers))), 0)

    def test_low(self):
        bet = Bet.create_low_range(value=100.)
        self.assertIsInstance(bet, Bet)
        self.assertEqual(bet.numbers, set(range(1, 19)))
    
    def test_high(self):
        bet = Bet.create_high_range(value=100.)
        self.assertIsInstance(bet, Bet)
        self.assertEqual(bet.numbers, set(range(19, 37)))


    def test_first_dozen(self):
        bet = Bet.create_first_dozen(value=100.)
        self.assertIsInstance(bet, Bet)
        self.assertEqual(bet.numbers, set(range(1, 13)))

    def test_second_dozen(self):
        bet = Bet.create_second_dozen(value=100.)
        self.assertIsInstance(bet, Bet)
        self.assertEqual(bet.numbers, set(range(13, 25)))

    def test_third_dozen(self):
        bet = Bet.create_third_dozen(value=100.)
        self.assertIsInstance(bet, Bet)
        self.assertEqual(bet.numbers, set(range(25, 37)))

    
    def test_first_line(self):
        bet = Bet.create_first_line(value=100.)
        self.assertIsInstance(bet, Bet)
        self.assertEqual(bet.numbers, set(range(1, 35, 3)))
    
    def test_second_line(self):
        bet = Bet.create_second_line(value=100.)
        self.assertIsInstance(bet, Bet)
        self.assertEqual(bet.numbers, set(range(2, 36, 3)))
    
    def test_third_line(self):
        bet = Bet.create_third_line(value=100.)
        self.assertIsInstance(bet, Bet)
        self.assertEqual(bet.numbers, set(range(3, 37, 3)))

    




    
    def test_get_random_number(self):
        spin = Roulette()
        bet = Bet.create_black(value=100.)
        self.assertIsInstance(spin, Roulette)
        for number in bet.numbers:
            if number == spin:
                self.assertEqual(number, spin)