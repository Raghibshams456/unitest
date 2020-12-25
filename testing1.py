from abcd import *
import unittest
class Testd(unittest.TestCase):
    def test_day(self):
        self.assertAlmostEqual(Solution({'2020-01-01':4,'2020-01-02':4,'2020-01-03':6,
                                        '2020-01-04':8,'2020-01-05':2,
                                         '2020-01-06':-6,'2020-01-07':2,'2020-01-08':-2}),{'Mon': -6, 
                                         'Tue': 2, 'Wed': 2, 'Thu': 4, 'Fri': 6, 'Sat': 8, 'Sun': 2})

if __name__ == '__main__':
    unittest.main()                    