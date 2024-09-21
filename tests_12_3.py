import unittest
import runner
import runner_and_tournament as RT


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        object1 = runner.Runner('Ron')
        for i in range(10):
            object1.walk()
        self.assertEqual(object1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        object2 = runner.Runner('Harry')
        for i in range(10):
            object2.run()
        self.assertEqual(object2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        object3 = runner.Runner('Kate')
        object4 = runner.Runner('Leo')
        for i in range(10):
            object3.run()
            object4.walk()
        self.assertNotEqual(object3.distance, object4.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = RT.Runner('Усэйн', 10)
        self.runner2 = RT.Runner('Андрей', 9)
        self.runner3 = RT.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for competition in cls.all_results.values():
            for keys, values in competition.items():
                print(keys, values)
            print('____________')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_competition1(self):
        distance1 = RT.Tournament(90, self.runner1, self.runner3)
        competition1 = distance1.start()
        TournamentTest.all_results[0] = competition1
        self.assertTrue(competition1[max(competition1.keys())] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_competition2(self):
        distance2 = RT.Tournament(90, self.runner2, self.runner3)
        competition2 = distance2.start()
        TournamentTest.all_results[1] = competition2
        self.assertTrue(competition2[max(competition2.keys())] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_competition3(self):
        distance3 = RT.Tournament(90, self.runner2, self.runner1, self.runner3)
        competition3 = distance3.start()
        TournamentTest.all_results[2] = competition3
        self.assertTrue(competition3[max(competition3.keys())] == 'Ник')


if __name__ == '__main__':
    unittest.main()
