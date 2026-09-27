import datetime
from database import add_task_to_db,get_tasks, update_task_in_db , delete_task_from_db
from statistics import show_statistics

def add_task():
    while True:
        task_name = input("Enter Task name: ").strip()
        if task_name:
            break 
        print("Task name cannot be empty.")

    while True:
        subject = input("Enter subject: ").strip()
        if subject:
            break
        print("Subject cannot be empty.")

    while True:
        priority = input("Enter Priority (High/Medium/Low): ").lower()
        if priority in ["high", "medium", "low"]:
            break

    print("Please enter High, Medium, or Low.")
    while True:
        deadline = input("Enter Deadline (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(deadline, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")

    print("\n")
    add_task_to_db(
        task_name,
        subject,
        priority,
        deadline,
        "pending"
    )
    print("Task added successfully")

def view_tasks():
    tasks_from_db = get_tasks()
    if len(tasks_from_db) == 0:
        print("No tasks available")
    else:
        print("\nYour tasks")
        today = datetime.date.today()
        for i, task in enumerate(tasks_from_db, start=1):
            deadline_date = datetime.datetime.strptime(task[4], "%Y-%m-%d").date()
            if deadline_date < today:
                deadline_status = "OVERDUE"
            elif deadline_date == today:
                deadline_status = "DUE TODAY"
            else:
                deadline_status = "UPCOMING"
            print("\nTask", i)
            print("Title    :", task[1])
            print("Subject  :", task[2])
            print("Priority :", task[3])
            print("Deadline :", task[4])
            print("Deadline status :", deadline_status)
            print("Status   :", task[5])  

def update_task():
    tasks_from_db = get_tasks()
    if len(tasks_from_db) == 0:
        print("No tasks available")
        return
    print("\nYour tasks")
    for i, task in enumerate(tasks_from_db, start=1):
        print(i, ":", task[1], "-", task[5])
    try:
        task_no = int(input("Enter task number to mark as complete: "))
    except ValueError:
        print("Enter only number")
        return
    if 1 <= task_no <= len(tasks_from_db):
        task_id = tasks_from_db[task_no - 1][0]
        update_task_in_db(task_id, "completed")
        print("Task marked as completed")
    else:
        print("Enter correct task number")        
    
def delete_task():
    tasks_from_db = get_tasks()
    if len(tasks_from_db) == 0:
        print("No tasks available")
        return
    print("\nYour tasks")
    for i, task in enumerate(tasks_from_db, start=1):
        print(i, ":", task[1], "-", task[5])
    try:
        task_no = int(input("Enter task number to delete: "))
    except ValueError:
        print("Enter only number")
        return
    if 1 <= task_no <= len(tasks_from_db):
        task_id = tasks_from_db[task_no - 1][0]
        delete_task_from_db(task_id)
        print("Task deleted successfully")
    else:
        print("Enter correct task number")  

def search_task():
    search = input("Enter task name to search: ")
    tasks_from_db = get_tasks()
    found = False
    for i, task in enumerate(tasks_from_db, start=1):
        if search.lower() in task[1].lower():
            print("\nTask", i)
            print("Title    :", task[1])
            print("Subject  :", task[2])
            print("Priority :", task[3])
            print("Deadline :", task[4])
            print("Status   :", task[5])
            found = True
    if not found:
        print("No matching task found")

def filter_tasks():
    print("\nFilter Tasks")
    print("1. pending")
    print("2. completed")
    print("3. high priority")
    print("4. medium priority")
    print("5. low priority")
    print("6. overdue")
    print("7. due today")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter only a number")
        return
    tasks_from_db = get_tasks()
    found = False
    today = datetime.date.today()
    for i, task in enumerate(tasks_from_db, start=1):
        deadline_date = datetime.datetime.strptime(task[4], "%Y-%m-%d").date()

        if choice == 1 and task[5] == "pending":
            print("\nTask", i, ":", task[1])
            found = True

        elif choice == 2 and task[5] == "completed":
            print("\nTask", i, ":", task[1])
            found = True

        elif choice == 3 and task[3].lower() == "high":
            print("\nTask", i, ":", task[1])
            found = True

        elif choice == 4 and task[3].lower() == "medium":
            print("\nTask", i, ":", task[1])
            found = True

        elif choice == 5 and task[3].lower() == "low":
            print("\nTask", i, ":", task[1])
            found = True

        elif choice == 6 and deadline_date < today:
            print("\nTask", i)
            print("Title    :", task[1])
            print("Deadline :", task[4])
            found = True

        elif choice == 7 and deadline_date == today:
            print("\nTask", i)
            print("Title    :", task[1])
            print("Deadline :", task[4])
            found = True
    if not found:
        print("No matching tasks found")

def exit_task():
    print("The program is exiting...")  
          

while True:
    print("----------------------")
    print("Student Study Tracker")
    print("----------------------")
    print("\n1.Add Task")
    print("2.View Task")
    print("3.Update Task")
    print("4.Delete Task")
    print("5.Search Task")
    print("6.Filter Tasks")
    print("7. Statistics")
    print("8.Exit")
    try:
        choice=int(input("Enter your choice: "))
    except ValueError:
        print("please enter a number")    
        continue

    if(choice==1):
        add_task()

    elif(choice==2):
        view_tasks()
             
    elif(choice==3):
        update_task()    

    elif(choice==4):
        delete_task()

    elif(choice==5):
        search_task()    

    elif(choice==6):
        filter_tasks()  

    elif(choice==7):
        show_statistics()      

    elif(choice==8):
        exit_task()
        break
    else:
        print("Enter valid choice ")
