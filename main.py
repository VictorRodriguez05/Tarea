from task_model import TaskModel

def main():
    task = TaskModel("Estudiar para el ezamen")
    print(f"Tarea creada: {task.get_task_name()} ")
    task.mark_as_complete()
    print(f"tarea completa: {task.is_completed()}")
    


if __name__=="__main__":
    main()    