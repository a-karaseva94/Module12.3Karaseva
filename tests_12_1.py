import unittest
import runner

# Задача "Проверка на выносливость"

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        object1 = runner.Runner('Ron')
        for i in range(10):
            object1.walk()
        self.assertEqual(object1.distance, 50)

    def test_run(self):
        object2 = runner.Runner('Harry')
        for i in range(10):
            object2.run()
        self.assertEqual(object2.distance, 100)

    def test_challenge(self):
        object3 = runner.Runner('Kate')
        object4 = runner.Runner('Leo')
        for i in range(10):
            object3.run()
            object4.walk()
        self.assertNotEqual(object3.distance, object4.distance)

if __name__ == '__main__':
    unittest.main()