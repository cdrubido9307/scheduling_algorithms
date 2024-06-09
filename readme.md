# Process Scheduling Algorithms

This project implements several process scheduling algorithms. The scheduler is assigned a predefined set of tasks and schedules the tasks based on the selected scheduling algorithm. Each task is assigned a priority and CPU burst time. The following scheduling algorithms are implemented:

- **First-Come, First-Served (FCFS)**: Schedules tasks in the order they request the CPU.
- **Shortest-Job-First (SJF)**: Schedules tasks in order of the length of the tasks' next CPU burst.
- **Priority Scheduling**: Schedules tasks based on priority.
- **Round-Robin (RR) Scheduling**: Each task is run for a time quantum (or for the remainder of its CPU burst).
- **Priority with Round-Robin**: Schedules tasks in order of priority and uses round-robin scheduling for tasks with equal priority.

## Task Structure

Tasks are represented with a name, priority, CPU burst time, and remaining burst time.

## Scheduler Base Class

The base class for all scheduling algorithms initializes the list of tasks and the current time. It includes a method to calculate and print the average turnaround time, waiting time, and response time for completed tasks.

## Implementation Details

### First-Come, First-Served (FCFS)

The FCFS scheduling algorithm schedules tasks in the order they arrive.

### Shortest-Job-First (SJF)

The SJF scheduling algorithm schedules tasks in order of the length of their next CPU burst.

### Priority Scheduling

The Priority scheduling algorithm schedules tasks based on their priority, with a higher numeric value indicating a higher priority.

### Round-Robin (RR) Scheduling

The Round-Robin scheduling algorithm runs each task for a specified time quantum or the remainder of its CPU burst.

### Priority with Round-Robin Scheduling

The Priority with Round-Robin scheduling algorithm schedules tasks in order of priority and uses round-robin scheduling for tasks with equal priority.

## Execution

To execute the scheduler, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the project directory.
4. Prepare a schedule of tasks in a file (e.g., `schedule.txt`) with the following format:
    ```
    T1, 4, 20
    T2, 2, 25
    T3, 3, 25
    T4, 3, 15
    T5, 10, 10
    ```
    Each line represents a task with a name, priority, and CPU burst time.
5. Run the scheduler with the desired algorithm. For example:
    ```
    python scheduler.py fcfs schedule.txt
    ```
    Replace `fcfs` with the desired algorithm (`sjf`, `priority`, `rr`, `priority_rr`).

## Example Usage

To run the FCFS scheduling algorithm with the given task schedule:

To run the Round-Robin scheduling algorithm with a time quantum of 10 milliseconds:

## Metrics

The scheduler will calculate and display the average turnaround time, waiting time, and response time for the completed tasks.

## Further Challenges

Two additional challenges include:
1. Fixing the possible race condition on the variable that assigns task identifiers in an SMP environment.
2. Calculating and displaying the average turnaround time, waiting time, and response time for each scheduling algorithm.
