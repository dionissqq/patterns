import time
import threading
import random
import unittest


# Master
class Master:
    def __init__(self, slaves):
        self.slaves = slaves

    def start_processing(self):
        print("Master: Starting processing")

        # Generate random tasks and distribute them to slaves
        tasks = self.generate_tasks()
        self.distribute_tasks(tasks)

        # Wait for all tasks to be completed
        while not self.is_all_tasks_completed():
            time.sleep(1)

        print("Master: All tasks completed")

    def generate_tasks(self):
        # Generate a list of random tasks
        tasks = []
        for i in range(10):
            task_id = i + 1
            task = f"Task {task_id}"
            tasks.append(task)
        return tasks

    def distribute_tasks(self, tasks):
        # Distribute tasks to slaves
        for i, task in enumerate(tasks):
            slave = self.slaves[i % len(self.slaves)]
            slave.receive_task(task)

    def is_all_tasks_completed(self):
        # Check if all slaves have completed their tasks
        for slave in self.slaves:
            if not slave.is_task_completed():
                return False
        return True


# Slave
class Slave:
    def __init__(self, name):
        self.name = name
        self.task = None
        self.task_completed = False

    def receive_task(self, task):
        # Receive a task from the master
        print(f"{self.name}: Received task - {task}")
        self.task = task

        # Start processing the task in a separate thread
        task_thread = threading.Thread(target=self.process_task)
        task_thread.start()

    def process_task(self):
        # Simulate task processing
        print(f"{self.name}: Processing task - {self.task}")
        time.sleep(random.randint(1, 5))
        print(f"{self.name}: Completed task - {self.task}")

        # Mark the task as completed
        self.task_completed = True

    def is_task_completed(self):
        # Check if the slave has completed its task
        return self.task_completed


# Unit Tests
class MasterSlaveTest(unittest.TestCase):
    def test_master_start_processing(self):
        slave1 = Slave("Slave 1")
        slave2 = Slave("Slave 2")

        master = Master([slave1, slave2])
        master.start_processing()

        self.assertTrue(slave1.is_task_completed())
        self.assertTrue(slave2.is_task_completed())


if __name__ == '__main__':
    unittest.main()
