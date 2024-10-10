from models import Task


class FakeDB:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        task.id = len(self.tasks) + 1
        self.tasks.append(task)
        return task

    def get_task(self, task_id: int):
        task = next((task for task in self.tasks if task.id == task_id), None)
        return task

    def get_tasks(self):
        return self.tasks

    def update_task(self, task_id: int, task_update):
        for task in self.tasks:
            if task.id == task_id:
                if task_update.title is not None:
                    task.title = task_update.title
                if task_update.description is not None:
                    task.description = task_update.description
                if task_update.completed is not None:
                    task.completed = task_update.completed
                return task
        return None

    def delete_all_tasks(self):
        self.tasks.clear()

    def delete_task(self, task_id: int):
        self.tasks = [task for task in self.tasks if task.id != task_id]

   


db = FakeDB()
