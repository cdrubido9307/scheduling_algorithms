import unittest
from scheduling_algorithms import Task, FCFS, SJF, Priority, RoundRobin, PriorityRoundRobin

class TestSchedulingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.tasks = [
            Task("T1", 4, 20),
            Task("T2", 2, 25),
            Task("T3", 3, 25),
            Task("T4", 3, 15),
            Task("T5", 10, 10)
        ]

    def test_fcfs(self):
        scheduler = FCFS(self.tasks)
        scheduler.run()
        self.assertEqual([task['task'] for task in scheduler.completed_tasks], ["T1", "T2", "T3", "T4", "T5"])

    def test_sjf(self):
        scheduler = SJF(self.tasks)
        scheduler.run()
        self.assertEqual([task['task'] for task in scheduler.completed_tasks], ["T5", "T4", "T1", "T2", "T3"])

    def test_priority(self):
        scheduler = Priority(self.tasks)
        scheduler.run()
        self.assertEqual([task['task'] for task in scheduler.completed_tasks], ["T5", "T1", "T3", "T4", "T2"])

if __name__ == '__main__':
    unittest.main()

