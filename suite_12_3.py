import unittest
import tests_12_1
import tests_12_2
import tests_12_3

# Задача "Заморозка кейсов":
# Часть 1. TestSuit
# Добавление тестов RunnerTest и TournamentTest в TestSuit

# RunTestSuite = unittest.TestSuite()
# RunTestSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
# RunTestSuite.addTests(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
#
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(RunTestSuite)

# Часть 2. Пропуск тестов
# по условию задачи, создаю еще один файл с изменениями RunnerTest и TournamentTest и запускаю RunTestSuite2
RunTestSuite2 = unittest.TestSuite()
RunTestSuite2.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
RunTestSuite2.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(RunTestSuite2)