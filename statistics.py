from database import get_tasks
import datetime


def show_statistics():
    tasks = get_tasks()

    total = len(tasks)

    completed = 0
    pending = 0
    overdue = 0

    today = datetime.date.today()

    for task in tasks:
        if task[5] == "completed":
            completed += 1
        elif task[5] == "pending":
            pending += 1

            deadline = datetime.datetime.strptime(
                task[4], "%Y-%m-%d"
            ).date()

            if deadline < today:
                overdue += 1

    if total > 0:
        completion_rate = (completed / total) * 100
    else:
        completion_rate = 0

    print("\n===== STUDY STATISTICS =====")
    print("Total tasks     :", total)
    print("Completed tasks :", completed)
    print("Pending tasks   :", pending)
    print("Overdue tasks   :", overdue)
    print("Completion rate :", round(completion_rate, 2), "%")


