from task_model import TaskModel

def main():
    task = TaskModel("Estudiar para el ezamen")
    print(f"Tarea creada: {task.get_task_name()} ")
    task.set_done()
    print(f"tarea completa: {task.is_done()}")
    task.remove_task()
    print(f"Tarea eliminada: {task.get_task_name()}")



if __name__=="__main__":
    main()    