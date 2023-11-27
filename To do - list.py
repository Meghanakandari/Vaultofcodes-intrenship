def display_menu():
    print("1. Add task")
    print("2. Delete task")
    print("3. View tasks")
    print("4. Mark task as complete")
    print("5. Exit")

def add_task(todo_list):
    task_description = input("Enter the task description: ")
    task = {"description": task_description, "completed": False}
    todo_list.append(task)
    print("Task added successfully!")

def delete_task(todo_list):
    if not todo_list:
        print("No tasks in the to-do list.")
        return

    view_tasks(todo_list)
    task_index = int(input("Enter the index of the task to delete: ")) - 1

    if 0 <= task_index < len(todo_list):
        del todo_list[task_index]
        print("Task deleted successfully.")
    else:
        print("Invalid index.")

def view_tasks(todo_list):
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{index}. {task['description']} - {status}")

def mark_complete(todo_list):
    if not todo_list:
        print("No tasks in the to-do list.")
        return

    view_tasks(todo_list)
    task_index = int(input("Enter the index of the task to mark as complete: ")) - 1

    if 0 <= task_index < len(todo_list):
        todo_list[task_index]["completed"] = True
        print("Task marked as complete.")
    else:
        print("Invalid index.")

def main():
    todo_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            delete_task(todo_list)
        elif choice == "3":
            view_tasks(todo_list)
        elif choice == "4":
            mark_complete(todo_list)
        elif choice == "5":
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
