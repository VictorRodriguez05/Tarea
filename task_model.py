class TaksModel:
    def __int__(self, task_name):
        self.task_name = task_name
        self.is_completd = False

    def get_task_name(self):
        return self.task_name
    
    def mark_as_complete(self):
        self.is_completd = True

    def is_completed(self):
        return self.is_completd    
        