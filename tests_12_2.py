import unittest
import runner_and_tournament as RT


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

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

    def test_competition1(self):
        distance1 = RT.Tournament(90, self.runner1, self.runner3)
        competition1 = distance1.start()
        TournamentTest.all_results[0] = competition1
        self.assertTrue(competition1[max(competition1.keys())] == 'Ник')

    def test_competition2(self):
        distance2 = RT.Tournament(90, self.runner2, self.runner3)
        competition2 = distance2.start()
        TournamentTest.all_results[1] = competition2
        self.assertTrue(competition2[max(competition2.keys())] =='Ник')

    def test_competition3(self):
        distance3 = RT.Tournament(90, self.runner2, self.runner1, self.runner3)
        competition3 = distance3.start()
        TournamentTest.all_results[2] = competition3
        self.assertTrue(competition3[max(competition3.keys())] == 'Ник')


if __name__ == '__main__':
    unittest.main()
