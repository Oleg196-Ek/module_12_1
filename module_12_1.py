import runner
import unittest

class  RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = runner.Runner("Anton")
        for i in range(10):#При замене количества вызовов метода - тест не пройден
            walker.walk()
        self.assertEqual(walker.distance, 50)# при замене значения 50 на 90
        # в панели Test Results результат - тест не пройден


    def test_run(self):
        walker = runner.Runner("Alex")
        for i in range(10):
            walker.run()
        self.assertEqual(walker.distance, 100)

    def test_challenge(self):
        run1 = runner.Runner('Elena')
        run2 = runner.Runner('Ekaterina')
        for i in range(10):
            run1.walk()
            run2.run()
        self.assertNotEqual(run1.distance, run2.distance)

if __name__ == '__main__':
    unittest.main()

