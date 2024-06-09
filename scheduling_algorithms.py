"""
Task Structure
"""
class Task:
    def __init__(self, name, priority, burst):
        self.name = name
        self.priority = priority
        self.burst = burst
        self.remaining_burst = burst

    def __repr__(self):
        return f"Task({self.name}, Priority: {self.priority}, Burst: {self.burst})"
    
"""
Scheduler Base Class
"""
class Scheduler:
    def __init__(self, tasks):
        self.tasks = tasks
        self.time = 0
        self.completed_tasks = []

    def run(self):
        raise NotImplementedError

    def calculate_metrics(self, completed_tasks):
        n = len(completed_tasks)
        total_turnaround_time = sum(task['completion_time'] for task in completed_tasks)
        total_waiting_time = sum(task['waiting_time'] for task in completed_tasks)
        total_response_time = sum(task['response_time'] for task in completed_tasks)

        avg_turnaround_time = total_turnaround_time / n
        avg_waiting_time = total_waiting_time / n
        avg_response_time = total_response_time / n

        print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
        print(f"Average Waiting Time: {avg_waiting_time:.2f}")
        print(f"Average Response Time: {avg_response_time:.2f}")


"""
First-Come, First-Served (FCFS)
"""
class FCFS(Scheduler):
    def run(self):
        for task in self.tasks:
            start_time = self.time
            self.time += task.burst
            completion_time = self.time
            turnaround_time = completion_time
            waiting_time = start_time
            response_time = start_time

            self.completed_tasks.append({
                'task': task.name,
                'start_time': start_time,
                'completion_time': completion_time,
                'turnaround_time': turnaround_time,
                'waiting_time': waiting_time,
                'response_time': response_time
            })

        self.calculate_metrics(self.completed_tasks)


"""
Shortest-Job-First (SJF)
"""
class SJF(Scheduler):
    def run(self):
        tasks = sorted(self.tasks, key=lambda x: x.burst)
        for task in tasks:
            start_time = self.time
            self.time += task.burst
            completion_time = self.time
            turnaround_time = completion_time
            waiting_time = start_time
            response_time = start_time

            self.completed_tasks.append({
                'task': task.name,
                'start_time': start_time,
                'completion_time': completion_time,
                'turnaround_time': turnaround_time,
                'waiting_time': waiting_time,
                'response_time': response_time
            })

        self.calculate_metrics(self.completed_tasks)

"""
Priority Scheduling
"""
class Priority(Scheduler):
    def run(self):
        tasks = sorted(self.tasks, key=lambda x: x.priority, reverse=True)
        for task in tasks:
            start_time = self.time
            self.time += task.burst
            completion_time = self.time
            turnaround_time = completion_time
            waiting_time = start_time
            response_time = start_time

            self.completed_tasks.append({
                'task': task.name,
                'start_time': start_time,
                'completion_time': completion_time,
                'turnaround_time': turnaround_time,
                'waiting_time': waiting_time,
                'response_time': response_time
            })

        self.calculate_metrics(self.completed_tasks)


"""
Round-Robin (RR)
"""
class RoundRobin(Scheduler):
    def __init__(self, tasks, time_quantum):
        super().__init__(tasks)
        self.time_quantum = time_quantum

    def run(self):
        task_queue = self.tasks[:]
        while task_queue:
            task = task_queue.pop(0)
            if task.remaining_burst > self.time_quantum:
                self.time += self.time_quantum
                task.remaining_burst -= self.time_quantum
                task_queue.append(task)
            else:
                self.time += task.remaining_burst
                completion_time = self.time
                turnaround_time = completion_time
                waiting_time = completion_time - task.burst
                response_time = self.time - task.burst

                self.completed_tasks.append({
                    'task': task.name,
                    'start_time': self.time - task.burst,
                    'completion_time': completion_time,
                    'turnaround_time': turnaround_time,
                    'waiting_time': waiting_time,
                    'response_time': response_time
                })

        self.calculate_metrics(self.completed_tasks)

"""
Priority with Round-Robin
"""
class PriorityRoundRobin(Scheduler):
    def __init__(self, tasks, time_quantum):
        super().__init__(tasks)
        self.time_quantum = time_quantum

    def run(self):
        priority_queues = {}
        for task in self.tasks:
            if task.priority not in priority_queues:
                priority_queues[task.priority] = []
            priority_queues[task.priority].append(task)

        while any(priority_queues.values()):
            for priority in sorted(priority_queues.keys(), reverse=True):
                task_queue = priority_queues[priority]
                new_queue = []
                while task_queue:
                    task = task_queue.pop(0)
                    if task.remaining_burst > self.time_quantum:
                        self.time += self.time_quantum
                        task.remaining_burst -= self.time_quantum
                        new_queue.append(task)
                    else:
                        self.time += task.remaining_burst
                        completion_time = self.time
                        turnaround_time = completion_time
                        waiting_time = completion_time - task.burst
                        response_time = self.time - task.burst

                        self.completed_tasks.append({
                            'task': task.name,
                            'start_time': self.time - task.burst,
                            'completion_time': completion_time,
                            'turnaround_time': turnaround_time,
                            'waiting_time': waiting_time,
                            'response_time': response_time
                        })
                priority_queues[priority] = new_queue

        self.calculate_metrics(self.completed_tasks)


# Sample tasks and executions:
if __name__ == "__main__":
    tasks = [
        Task("T1", 4, 20),
        Task("T2", 2, 25),
        Task("T3", 3, 25),
        Task("T4", 3, 15),
        Task("T5", 10, 10)
    ]

    print("FCFS Scheduling")
    fcfs = FCFS(tasks[:])
    fcfs.run()

    print("\nSJF Scheduling")
    sjf = SJF(tasks[:])
    sjf.run()

    print("\nPriority Scheduling")
    priority = Priority(tasks[:])
    priority.run()

    print("\nRound-Robin Scheduling")
    rr = RoundRobin(tasks[:], time_quantum=10)
    rr.run()

    print("\nPriority Round-Robin Scheduling")
    prr = PriorityRoundRobin(tasks[:], time_quantum=10)
    prr.run()
