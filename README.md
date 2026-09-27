# StudyTrack

StudyTrack is a command-line Student Productivity Management System built with Python and SQLite.

It helps students organize study tasks, manage deadlines, track completion, and monitor productivity through simple statistics.

## Features

- Add study tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Search tasks by name
- Filter tasks by:
  - Status
  - Priority
  - Overdue tasks
  - Tasks due today
- Deadline tracking
- Overdue task detection
- Productivity statistics
- Completion rate calculation
- SQLite persistent storage
- Input validation

## Technologies Used

- Python
- SQLite
- Git
- GitHub

## How It Works

The application is divided into three main Python modules:

- `main.py` — Handles the user interface, menu, input validation, task operations, searching, and filtering.
- `database.py` — Handles SQLite database creation and CRUD operations.
- `statistics.py` — Calculates productivity statistics such as completed, pending, overdue tasks, and completion rate.

Task data is stored in SQLite, allowing tasks to remain available even after restarting the application.

## Project Structure

```text
StudyTrack/
│
├── main.py
├── database.py
├── statistics.py
├── README.md
└── .gitignore